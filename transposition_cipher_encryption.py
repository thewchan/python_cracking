"""transposition_cipher_encryption.py - Encrypt text messages via Transposition
 Cipher.
Use via ./python transposition_cipher_encryption.py KEY MESSAGE.
KEY = int that gives the key for transposition Cipher encryption or decryption
MESSAGE = str of message to encrypt/decrypt via transposition Cipher, enclosed
 with quotes.
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


def encrypt_message(key, message):
    """Encrypt message via transposition cipher with given key."""
    ciphertext = [''] * key

    for column in range(key):
        current_index = column

        while current_index < len(message):
            ciphertext[column] += message[current_index]
            current_index += key

    return ''.join(ciphertext)


def main():
    """Perform encryption."""
    key, message = get_parameters()
    ciphertext = encrypt_message(key, message)

    print(f'"{ciphertext}"')
    pyperclip.copy(ciphertext)


if __name__ == '__main__':
    main()
