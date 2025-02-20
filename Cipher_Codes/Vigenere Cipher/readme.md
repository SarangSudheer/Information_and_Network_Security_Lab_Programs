# Vigenère Cipher Implementation

### Vigenère Cipher
- The Vigenère cipher is a method of encrypting alphabetic text by using a series of Caesar ciphers based on letters of a keyword.
- It is a polyalphabetic substitution cipher that improves upon the simple Caesar cipher by using multiple shift values.
- The strength of this cipher lies in the complexity introduced by the keyword.

## Features
- Encrypts messages using the Vigenère cipher technique.
- Decrypts encrypted messages back to their original form.
- Automatically extends the key to match the length of the message.
- Works only with uppercase letters (spaces are removed automatically).

## How to Run the Code

### Run Live
[Click here to Run Live](https://colab.research.google.com/drive/1dmeXx52QAguWlfhFCuS2RsiU1htrim89?usp=sharing)

### Running Locally
1. Clone the repository:
   ```sh
   gh repo clone YourUsername/Vigenere-Cipher
   ```
2. Navigate to the directory:
   ```sh
   cd Cipher_Codes/Vigenere Cipher
   ```
3. Run the script:
   ```sh
   python vigenere_cipher.py
   ```

### Running on GitHub Codespaces
1. Open the repository on GitHub.
2. Click on the **Codespaces** tab.
3. Select **New Codespace** to launch an online development environment.
4. Run the script inside the terminal.

## Output
```
Enter the msg: HELLO
Enter the key: KEY
Ciphertext: RIJVS
Plaintext: HELLO
```


