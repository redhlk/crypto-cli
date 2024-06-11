class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, plaintext):
        encrypted = ""
        for char in plaintext:
            if char.isalpha():
                shift = self.shift % 26
                shifted = ord(char) + shift
                if char.islower():
                    if shifted > ord("z"):
                        shifted -= 26
                    encrypted += chr(shifted)
                elif char.isupper():
                    if shifted > ord("Z"):
                        shifted -= 26
                    encrypted += chr(shifted)
            else:
                encrypted += char
        return encrypted

    def decrypt(self, ciphertext):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                shift = self.shift % 26
                shifted = ord(char) - shift
                if char.islower():
                    if shifted < ord("a"):
                        shifted += 26
                    decrypted += chr(shifted)
                elif char.isupper():
                    if shifted < ord("A"):
                        shifted += 26
                    decrypted += chr(shifted)
            else:
                decrypted += char
        return decrypted
