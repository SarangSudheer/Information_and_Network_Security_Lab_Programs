# Hill Cipher Implementation

### Hill Cipher 
- The Hill cipher is a polygraphic substitution cipher based on linear algebra.
- It uses matrix multiplication to transform blocks of plaintext into ciphertext.
- The encryption process involves multiplying a key matrix with a message matrix and taking modulo 26 to get the ciphertext.
- Decryption requires finding the inverse of the key matrix, which is used to recover the original plaintext.

## Features
- Encrypts messages using the Hill cipher.
- Supports variable-sized key matrices.
- Automatically handles padding when the message length is not a multiple of the matrix size.

## How to Run the Code

### Run Live
[Click here to Run Live](https://colab.research.google.com/drive/1GFhJ-eogJOknj_7B6-wgqosgZrnddvMU?usp=sharing)

### Running Locally
1. Clone the repository:
   ```sh
   gh repo clone YourUsername/Hill-Cipher-Implementation
   ```
2. Navigate to the directory:
   ```sh
   cd Cipher_Codes/Hill Cipher
   ```
3. Run the script:
   ```sh
   python hill_cipher.py
   ```

### Running on GitHub Codespaces
1. Open the repository on GitHub.
2. Click on the **Codespaces** tab.
3. Select **New Codespace** to launch an online development environment.
4. Run the script inside the terminal.

## Output
```
Enter the message: HELLO
Enter the key: GYBNQKURP
Encrypted: TFJJZX
```

