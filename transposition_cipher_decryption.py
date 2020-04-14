"""transposition_cipher_decryption.py - Encrypt text messages via Transposition
 Cipher.
Use via ./python transposition_cipher_decryption.py KEY CIPHERTEXT.
KEY = int that gives the key for transposition Cipher decryption or decryption
CIPHERTEXT = str of message to encrypt/decrypt via transposition Cipher,
 enclosed with quotes.
"""
import sys
import math
import logging
import pyperclip


logging.basicConfig(
    level=logging.DEBUG,
    format='    {asctime} - {levelname} - {message}',
    style='{',
    )
logging.disable(logging.CRITICAL)


def get_parameters():
    """Check for user arguments validity and return key, and message."""
    logging.debug(
        'KEY = %s MESSAGE = %s',
        sys.argv[1], sys.argv[2],
        )
    if len(sys.argv) < 3:
        print('This program needs exactly 2 parameters: KEY, and MESSAGE.')
        sys.exit(1)
    else:
        try:
            key = int(sys.argv[1])
        except ValueError as ex:
            print(f'{ex} KEY must be an integer.')
            sys.exit(1)
        message = sys.argv[2]
        return key, message


def decrypt_message(key, message):
    """Decrypt message via transposition cipher with given key."""
    num_columns = int(math.ceil(len(message) / float(key)))
    num_rows = key
    num_shaded_boxes = (num_columns * num_rows) - len(message)
    plaintext = [''] * num_columns
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if (
            (column == num_columns) or
            (column == num_columns - 1 and
                row >= (num_rows - num_shaded_boxes))
                ):
            column = 0
            row += 1

    return ''.join(plaintext)


def main():
    """Perform decryption."""
    key, message = get_parameters()
    plaintext = decrypt_message(key, message)

    print(f'"{plaintext}"')
    pyperclip.copy(plaintext)


if __name__ == '__main__':
    main()
