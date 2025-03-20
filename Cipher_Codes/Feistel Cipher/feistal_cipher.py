import random

# Sample round function (simple XOR-based function)
def round_function(right, key):
    return right ^ key  # XOR operation

# Convert text to binary numbers for processing
def text_to_num(msg):
    bin_msg = ''.join(format(ord(c), '08b') for c in msg)  # Convert each char to 8-bit binary
    mid = len(bin_msg) // 2  # Split point
    L, R = bin_msg[:mid], bin_msg[mid:]  # Split halves
    return int(L, 2), int(R, 2), len(bin_msg)  # Return halves + total bit length

# Convert binary number back to text
def num_to_text(num, bit_length):
    bin_str = format(num, f'0{bit_length}b')  # Convert to binary with fixed length
    chars = [chr(int(bin_str[i:i+8], 2)) for i in range(0, len(bin_str), 8)]  # Convert chunks of 8 bits
    return ''.join(chars)

# Feistel Cipher function
def feistel_cipher(plaintext, keys, rounds=4):
    L, R, bit_length = text_to_num(plaintext)  # Convert text to numeric halves

    print(f"Initial L: {L}, R: {R}")

    # Encryption rounds
    for i in range(rounds):
        temp = R
        R = L ^ round_function(R, keys[i])  # L XOR F(R, Key)
        L = temp  # Swap halves
        print(f"Round {i+1}: L={L}, R={R}")

    # Final ciphertext (combine L and R)
    ciphertext = (L << (bit_length // 2)) | R  # Correct bit shifting
    print(ciphertext)
    return num_to_text(ciphertext, bit_length)

# Generate random round keys
def generate_keys(rounds):
    return [random.randint(0, 255) for _ in range(rounds)]  # 8-bit keys

# Decryption function (reverses encryption)
def feistel_decrypt(ciphertext, keys, rounds=4):
    L, R, bit_length = text_to_num(ciphertext)  # Convert back to halves

    print(f"Initial L: {L}, R: {R}")

    # Reverse rounds for decryption
    for i in range(rounds - 1, -1, -1):  # Reverse order of keys
        temp = L
        L = R ^ round_function(L, keys[i])  # Reverse process
        R = temp  # Swap halves
        print(f"Round {rounds - i}: L={L}, R={R}")

    # Combine back
    plaintext = (L << (bit_length // 2)) | R
    print(plaintext)
    return num_to_text(plaintext, bit_length)

# Example usage
plaintext = "sarang"  # Example input
keys = generate_keys(16)  # Generate 4 random keys

print("\nEncryption Process:")
ciphertext = feistel_cipher(plaintext, keys,16)
print(f"Ciphertext: {ciphertext}")

print("\nDecryption Process:")
decrypted_text = feistel_decrypt(ciphertext, keys,16)
print(f"Decrypted Text: {decrypted_text}")

# Ensure decryption is correct
assert plaintext == decrypted_text, "Decryption failed!"
