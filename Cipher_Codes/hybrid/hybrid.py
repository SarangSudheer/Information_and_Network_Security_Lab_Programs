from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import random

def pad(data):
    """Pads data to be a multiple of 16 bytes"""
    padding_len = 16 - (len(data) % 16)
    return data + bytes([padding_len] * padding_len)

def unpad(data):
    """Removes padding"""
    return data[:-data[-1]]

def generate_permutation(block_size=16):
    """Generates a random permutation of bytes within a block"""
    permutation = list(range(block_size))
    random.shuffle(permutation)
    return permutation

def apply_permutation_blockwise(data, permutation, block_size=16):
    """Applies a given permutation to each block of the data"""
    permuted_data = bytearray(len(data))
    for i in range(0, len(data), block_size):
        block = data[i:i + block_size]
        permuted_data[i:i + block_size] = bytes(block[j] for j in permutation)
    return bytes(permuted_data)

def reverse_permutation(permutation):
    """Generates the inverse of a given permutation"""
    reverse_perm = [0] * len(permutation)
    for i, p in enumerate(permutation):
        reverse_perm[p] = i
    return reverse_perm

def encrypt(plaintext, key):
    """Encrypts data using AES-128 and applies transposition"""
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(plaintext.encode())
    encrypted = cipher.encrypt(padded_data)
    
    # Generate a random permutation
    permutation = generate_permutation()
    permuted_encrypted = apply_permutation_blockwise(encrypted, permutation)
    
    return permuted_encrypted, permutation

def decrypt(permuted_encrypted, key, permutation):
    """Decrypts data by reversing transposition and applying AES-128 decryption"""
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Reverse the permutation
    reverse_perm = reverse_permutation(permutation)
    reordered_encrypted = apply_permutation_blockwise(permuted_encrypted, reverse_perm)
    
    decrypted_padded = cipher.decrypt(reordered_encrypted)
    decrypted = unpad(decrypted_padded)
    
    return decrypted.decode()

key = get_random_bytes(16)  # AES-128 requires a 16-byte key
plaintext = input("Enter text to encrypt: ")

ciphertext, permutation = encrypt(plaintext, key)
print(f"Encrypted (Hex): {ciphertext.hex()}")

print("----------------------------------------------------------------------")

ciphertext_input = bytes.fromhex(input("Enter ciphertext to decrypt (Hex): "))
decrypted_text = decrypt(ciphertext_input, key, permutation)

print(f"Decrypted: {decrypted_text}")
