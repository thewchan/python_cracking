"""ceasar_cipher.py - Encrypt/Decrypt text messages via Ceasar Cipher.
Use via ./python ceasar_cipher.py MODE KEY MESSAGE.
MODE = str that indicates encryption or decryption via 'encrypt' or 'decrypt'.
KEY = int that gives the key for Cesar Cipher encryption or decryption
MESSAGE = str of message to encrypt/decrypt via Cesar Cipher, enclosed with
q
"""
import sys
import logging
import pyperclip


logging.basicConfig(
    level=logging.DEBUG,
    format='    {asctime} - {levelname} - {message}',
    style='{',
    )
logging.disable(logging.CRITICAL)

SYMBOLS = (
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    )


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
        mode = sys.argv[1]
        message = sys.argv[3]
        return mode, key, message


def main():
    """Perform encryption or decryption"""
    mode, key, message = get_parameters()
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)

            if mode == 'encrypt':
                translated_index = symbol_index + key
            elif mode == 'decrypt':
                translated_index = symbol_index - key

            if translated_index >= len(SYMBOLS):
                translated_index -= len(SYMBOLS)
            elif translated_index < 0:
                translated_index += len(SYMBOLS)

            translated += SYMBOLS[translated_index]

        else:
            translated += symbol

    print(translated)
    pyperclip.copy(translated)


if __name__ == '__main__':
    main()
