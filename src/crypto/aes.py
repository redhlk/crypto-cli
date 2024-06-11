import os


class AESEncryption:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        padded_text = self._pad(plaintext)
        ciphertext = self._xor_bytes(padded_text.encode("utf-8"), self.key)
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = self._xor_bytes(ciphertext, self.key).decode("utf-8")
        return self._unpad(plaintext)

    def _xor_bytes(self, data, key):
        return bytes(a ^ b for a, b in zip(data, key))

    def _pad(self, s):
        pad_len = 16 - len(s) % 16
        return s + pad_len * chr(pad_len)

    def _unpad(self, s):
        pad_len = ord(s[-1])
        return s[:-pad_len]
