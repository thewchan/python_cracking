"""Encrypt or decrypt text files via transposition cipher."""
import time
import os
import sys
import logging
import transposition_cipher_encryption
import transposition_cipher_decryption


logging.basicConfig(
    level=logging.DEBUG,
    format='    {asctime} - {levelname} - {message}',
    style='{',
    )
logging.disable(logging.CRITICAL)


def get_parameters():
    """Check for user arguments validity and return mode, key and message."""
    logging.debug(
        'MODE = %s KEY = %s FILE = %s',
        sys.argv[1], sys.argv[2], sys.argv[3],
        )

    if len(sys.argv) < 4:
        print('This program needs exactly 3 parameters: MODE, KEY, FILE.')
        sys.exit(1)

    elif not (
            sys.argv[1].lower() == 'encrypt' or
            sys.argv[1].lower() == 'decrypt'):
        print('Argument MODE must be either "decrypt" or "encrypt".')
        sys.exit(1)

    else:

        try:
            key = int(sys.argv[2])

        except ValueError as ex:
            print(f'{ex} KEY must be an integer.')
            sys.exit(1)

        try:
            file_test = open(sys.argv[3])
            file_test.close()

        except FileNotFoundError as ex:
            print(f'{ex} Enter valid FILE argument.')
            sys.exit(1)

        mode = sys.argv[1]
        input_filename = sys.argv[3]
        return mode, key, input_filename


def main():
    mode, key, input_filename = get_parameters()
    start_time = time.time()
    output_filename = ''.join([
        os.path.splitext(input_filename)[0],
        f'_{mode}ed',
        os.path.splitext(input_filename)[1]
        ])

    with open(input_filename, encoding="utf8") as f:
        content = f.read()

    print(f'{mode.title()}ing:')

    if mode.lower() == 'encrypt':
        translated = transposition_cipher_encryption.encrypt_message(
            key, content
            )
    elif mode.lower() == 'decrypt':
        translated = transposition_cipher_decryption.decrypt_message(
            key, content
            )

    total_time = round(time.time() - start_time, 2)
    print(f'{mode.title()}ion time: {total_time} seconds.')

    with open(output_filename, 'w', encoding="utf8") as f:
        f.write(translated)

    print(f'{mode.title()}ion complete. File saved as {output_filename}.')
    print(f'Total characters {mode}ed: {len(content)}.')


if __name__ == '__main__':
    main()
