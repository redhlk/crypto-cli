class VigenereCipher:
    def __init__(self, key):
        self.key = key

    def _extend_key(self, length):
        return (self.key * (length // len(self.key) + 1))[:length]

    def encrypt(self, plaintext):
        key = self._extend_key(len(plaintext))
        encrypted = ""
        for p, k in zip(plaintext, key):
            if p.isalpha():
                shift = ord(k.lower()) - ord('a')
                shifted = ord(p) + shift
                if p.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    encrypted += chr(shifted)
                elif p.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    encrypted += chr(shifted)
            else:
                encrypted += p
        return encrypted

    def decrypt(self, ciphertext):
        key = self._extend_key(len(ciphertext))
        decrypted = ""
        for c, k in zip(ciphertext, key):
            if c.isalpha():
                shift = ord(k.lower()) - ord('a')
                shifted = ord(c) - shift
                if c.islower():
                    if shifted < ord('a'):
                        shifted += 26
                    decrypted += chr(shifted)
                elif c.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                    decrypted += chr(shifted)
            else:
                decrypted += c
        return decrypted
