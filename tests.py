from src.caesar_cipher import CaesarCipher
from src.vigenere_cipher import VigenereCipher
from src.rsa import generate_keypair, encrypt as rsa_encrypt, decrypt as rsa_decrypt
from src.aes import AESEncryption
import os

def test_caesar_cipher():
    caesar = CaesarCipher(4)
    plaintext = "Hell hi or buddy o, World!"
    encrypted = caesar.encrypt(plaintext)
    decrypted = caesar.decrypt(encrypted)
    print(f"Caesar Cipher:\nPlaintext: {plaintext}\nEncrypted: {encrypted}\nDecrypted: {decrypted}\n")

def test_vigenere_cipher():
    vigenere = VigenereCipher("KEY")
    plaintext = "Hello, World!"
    encrypted = vigenere.encrypt(plaintext)
    decrypted = vigenere.decrypt(encrypted)
    print(f"Vigenere Cipher:\nPlaintext: {plaintext}\nEncrypted: {encrypted}\nDecrypted: {decrypted}\n")

def test_rsa():
    p = 61
    q = 53
    public, private = generate_keypair(p, q)
    plaintext = "Hello, World!"
    encrypted = rsa_encrypt(public, plaintext)
    decrypted = rsa_decrypt(private, encrypted)
    print(f"RSA Encryption:\nPlaintext: {plaintext}\nEncrypted: {encrypted}\nDecrypted: {decrypted}\n")

def test_aes():
    key = os.urandom(16)
    aes = AESEncryption(key)
    plaintext = "Hello, World!"
    encrypted = aes.encrypt(plaintext)
    decrypted = aes.decrypt(encrypted)
    print(f"AES Encryption:\nPlaintext: {plaintext}\nEncrypted: {encrypted}\nDecrypted: {decrypted}\n")

if __name__ == "__main__":
    test_caesar_cipher()
    test_vigenere_cipher()
    test_rsa()
    test_aes()
