"""Decyrpt text string via brute-force dictionary crack of transposition
 cipher text.
 Use by: python hacker.py MESSAGE DICT_PATH
 MESSAGE = Cipher text enclosed in quotes.
 DICT_PATH = Relative or absolute path to dictionary file.
 """
import sys
import os
import pyperclip
import detect_english
import transposition_cipher_decryption


def hack_transposition(message, dict_path):
    """Calls transposition_cipher_decryption module and dectect_english module
     too brute-force decrypt cipher text.
    """
    print('Decryption in process. Press Ctrl-C to interrupt and exit.')

    for key in range(1, len(message)):
        print(f'Trying key: {key}')
        decrypted_text = transposition_cipher_decryption.decrypt_message(
            key, message
            )

        if detect_english.is_english(decrypted_text, dict_path):
            print('\nPossible decryption:')
            print(f'Key {key}: {decrypted_text[:100]}')
            return decrypted_text

    print('Decryption unsuccessful.')
    return None


def main():
    """Check validity of arguments and run main program."""
    if len(sys.argv) < 3:
        print('This program needs exactly 2 argument: MESSAGE, DICT_PATH')
        sys.exit(1)
    elif not os.path.exists(sys.argv[2]):
        print('Invalid path to dictionary file.')
        sys.exit(1)

    message = sys.argv[1]
    dict_path = sys.argv[2]
    decrypted_message = hack_transposition(message, dict_path)

    if decrypted_message is None:
        sys.exit(0)
    else:
        print('Decrypted message copied to clipboard.')
        pyperclip.copy(decrypted_message)


if __name__ == '__main__':
    main()
