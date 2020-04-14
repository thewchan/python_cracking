import sys
import random
import logging
import pyperclip
import cryptomath


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmonpqrdtuvwxyz1234567890 !?.'
logging.basicConfig(
    level=logging.DEBUG,
    format='    {asctime} - {levelname} - {message}',
    style='{',
    )
logging.disable(logging.CRITICAL)


def get_parameters():
    """Check for user arguments validity and return mode, key and message."""
    logging.debug(
        'MODE = %s KEY = %s MESSAGE = %s',
        sys.argv[1], sys.argv[2], sys.argv[3],
        )
    if len(sys.argv) < 4:
        print('This program needs exactly 3 parameters: MODE, KEY, MESSAGE.')
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
        mode = sys.argv[1].lower()
        message = sys.argv[3]
        return mode, key, message


def get_key_parts(key):
    key_A = key // len(SYMBOLS)
    key_B = key % len(SYMBOLS)
    return (key_A, key_B)


def check_keys(key_A, key_B, mode):
    if key_A == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak if key_A is 1. Choose a different key.')
    if key_B == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if key_B is 0. Choose a different key.')
    if key_A < 0 or key_B < 0 or key_B > (len(SYMBOLS) - 1):
        sys.exit(
            f'key_A must be greater than 0 and key_B must be between 0 and '
            f'{len(SYMBOLS) - 1}'
            )


def encrypt_message(key, message):
    key_A, key_B = get_key_parts(key)
    check_keys(key_A, key_B, 'encrypt')
    ciphertext = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[
                ((symbol_index * key_A) + key_B) % len(SYMBOLS)
                    ]
        else:
            ciphertext += symbol

    return ciphertext


def decrypt_message(key, message):
    key_A, key_B = get_key_parts(key)
    check_keys(key_A, key_B, 'decrypt')
    plaintext = ''
    mod_invese_key_A = cryptomath.find_mod_inverse(key_A, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[
                (symbol_index - key_B) * mod_invese_key_A % len(SYMBOLS)
                    ]
        else:
            plaintext += symbol

    return plaintext


def get_random_key():
    while True:
        key_A = random.randint(2, len(SYMBOLS))
        key_B = random.randint(2, len(SYMBOLS))

        if cryptomath.gcd(key_A, len(SYMBOLS)) == 1:
            return (key_A * len(SYMBOLS)) + key_B


def main():
    mode, key, message = get_parameters()

    if mode == 'encrypt':
        translated = encrypt_message(key, message)
    elif mode == 'decrypt':
        translated = decrypt_message(key, message)

    print(f'Key: {key}')
    print(f'{mode.title()}ed text:')
    print(translated)
    pyperclip.copy(translated)
    print(f'Full {mode.title()}ed text copied to clipboard.')


if __name__ == '__main__':
    main()
