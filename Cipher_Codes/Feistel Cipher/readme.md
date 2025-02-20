# Feistel Cipher Implementation

### Feistel Cipher
- The Feistel cipher is a symmetric structure used in block cipher algorithms.
- It divides the plaintext into two halves and processes them through multiple rounds of encryption.
- Each round involves operations like bitwise XOR, addition, and key mixing.

## Features
- Converts plaintext into an 8-bit binary representation.
- Splits the binary representation into left and right halves for encryption.
- Uses a key to perform bitwise operations for encryption and decryption.
- Reconstructs the original plaintext after decryption.

## How to Run the Code

### Run Live
[Click here to Run Live](https://colab.research.google.com/drive/1UIt2rBrqUk2794_D1do4lDi_MEYyVFun?usp=sharing)

### Running Locally
1. Clone the repository:
   ```sh
   gh repo clone SarangSudheer/Information_and_Network_Security_Lab_Programs
   ```
2. Navigate to the directory:
   ```sh
   cd Cipher_Codes/Feistel Cipher
   ```
3. Run the script:
   ```sh
   python feistel_cipher.py
   ```

### Running on GitHub Codespaces
1. Open the repository on GitHub.
2. Click on the **Codespaces** tab.
3. Select **New Codespace** to launch an online development environment.
4. Run the script inside the terminal.

## Output
```
Enter a string : HELLO
Enter a key : KEY
Cipher: 110010101010...
Plaintext: HELLO
```


