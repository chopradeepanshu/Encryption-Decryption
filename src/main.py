from src import Encryption, Decryption


def main():
    message = input("Enter your message")
    encrypted_message = Encryption.Encryption.encrypt(message)
    print(encrypted_message)
    decrypted_message = Decryption.Decryption.decrypt(encrypted_message)
    print(decrypted_message)


if __name__ == "__main__":
    main()
