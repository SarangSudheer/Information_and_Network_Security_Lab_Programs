import numpy as np
from sympy import Matrix

def vigenere_encrypt(text, key):
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    return ''.join(chr((ord(p) + ord(k)) % 26 + 65) for p, k in zip(text, key))

def vigenere_decrypt(cipher, key):
    key = (key * (len(cipher) // len(key) + 1))[:len(cipher)]
    return ''.join(chr((ord(c) - ord(k)) % 26 + 65) for c, k in zip(cipher, key))

def hill_encrypt(text, key_matrix):
    n = len(key_matrix)
    text_vector = [ord(c) - 65 for c in text]
    padded_vector = text_vector + [0] * (n - len(text_vector) % n)
    encrypted_vector = (np.dot(np.reshape(padded_vector, (-1, n)), key_matrix) % 26).flatten()
    return ''.join(chr(c + 65) for c in encrypted_vector)

def hill_decrypt(cipher, key_matrix):
    n = len(key_matrix)
    cipher_vector = [ord(c) - 65 for c in cipher]
    key_inverse = Matrix(key_matrix).inv_mod(26)
    decrypted_vector = (np.dot(np.reshape(cipher_vector, (-1, n)), key_inverse) % 26).flatten()
    return ''.join(chr(c + 65) for c in decrypted_vector)

def playfair_encrypt(text, key_square):
    text = text.replace('J', 'I')
    text_pairs = [(text[i], text[i + 1]) for i in range(0, len(text), 2)]
    cipher_text = ''
    for a, b in text_pairs:
        ax, ay = divmod(key_square.index(a), 5)
        bx, by = divmod(key_square.index(b), 5)
        if ax == bx:
            cipher_text += key_square[ax * 5 + (ay + 1) % 5] + key_square[bx * 5 + (by + 1) % 5]
        elif ay == by:
            cipher_text += key_square[((ax + 1) % 5) * 5 + ay] + key_square[((bx + 1) % 5) * 5 + by]
        else:
            cipher_text += key_square[ax * 5 + by] + key_square[bx * 5 + ay]
    return cipher_text

def playfair_decrypt(cipher, key_square):
    cipher_pairs = [(cipher[i], cipher[i + 1]) for i in range(0, len(cipher), 2)]
    decrypted_text = ''
    for a, b in cipher_pairs:
        ax, ay = divmod(key_square.index(a), 5)
        bx, by = divmod(key_square.index(b), 5)
        if ax == bx:
            decrypted_text += key_square[ax * 5 + (ay - 1) % 5] + key_square[bx * 5 + (by - 1) % 5]
        elif ay == by:
            decrypted_text += key_square[((ax - 1) % 5) * 5 + ay] + key_square[((bx - 1) % 5) * 5 + by]
        else:
            decrypted_text += key_square[ax * 5 + by] + key_square[bx * 5 + ay]
    return decrypted_text

def hybrid_encrypt(plaintext, vigenere_key, hill_matrix, playfair_square):
    step1 = vigenere_encrypt(plaintext, vigenere_key)
    step2 = hill_encrypt(step1, hill_matrix)
    step3 = playfair_encrypt(step2, playfair_square)
    return step3

def hybrid_decrypt(ciphertext, vigenere_key, hill_matrix, playfair_square):
    step1 = playfair_decrypt(ciphertext, playfair_square)
    step2 = hill_decrypt(step1, hill_matrix)
    step3 = vigenere_decrypt(step2, vigenere_key)
    return step3

plaintext = "HYBRIDCIPHEREXAMPLE"
vigenere_key = "SECUREKEY"
hill_matrix = np.array([[3, 2], [5, 7]])
playfair_square = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

encrypted = hybrid_encrypt(plaintext, vigenere_key, hill_matrix, playfair_square)
decrypted = hybrid_decrypt(encrypted, vigenere_key, hill_matrix, playfair_square)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
