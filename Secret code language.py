class SecretCode:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.reverse_alphabet = self.alphabet[::-1]
        self.key = 3

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                if char.isupper():
                    index = self.alphabet.index(char.lower())
                    encrypted_char = self.reverse_alphabet[index]
                    encrypted_message += encrypted_char.upper()
                else:
                    index = self.alphabet.index(char)
                    encrypted_char = self.reverse_alphabet[index]
                    encrypted_message += encrypted_char
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, message):
        decrypted_message = ""
        for char in message:
            if char.isalpha():
                if char.isupper():
                    index = self.reverse_alphabet.index(char.lower())
                    decrypted_char = self.alphabet[index]
                    decrypted_message += decrypted_char.upper()
                else:
                    index = self.reverse_alphabet.index(char)
                    decrypted_char = self.alphabet[index]
                    decrypted_message += decrypted_char
            else:
                decrypted_message += char
        return decrypted_message

    def run(self):
        while True:
            print("\n1. Encrypt Message")
            print("2. Decrypt Message")
            print("3. Change Key")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                message = input("Enter message to encrypt: ")
                print(f"Encrypted message: {self.encrypt(message)}")
            elif choice == "2":
                message = input("Enter message to decrypt: ")
                print(f"Decrypted message: {self.decrypt(message)}")
            elif choice == "3":
                self.key = int(input("Enter new key: "))
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    secret_code = SecretCode()
    secret_code.run()