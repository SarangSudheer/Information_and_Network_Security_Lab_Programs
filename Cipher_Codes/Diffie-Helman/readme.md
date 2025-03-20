# Diffie-Hellman Key Exchange Implementation

## Diffie-Hellman Algorithm
- Diffie-Hellman is a key exchange algorithm that allows two parties to securely share a cryptographic key over a public channel.
- It relies on the mathematical properties of modular exponentiation and discrete logarithms.

## Features
- Computes public keys for two users.
- Generates a shared secret key between two communicating parties.
- Ensures secure key exchange without transmitting the private keys.

## How to Run the Code

### Run Live
[Click here to Run Live](https://colab.research.google.com/drive/11-QuizPirWj9fkvr1i7CmgDxJXaZ7zD4?usp=sharing)

### Running Locally
1. Clone the repository:
   ```sh
   gh repo clone SarangSudheer/Information_and_Network_Security_Lab_Programs
   ```
2. Navigate to the directory:
   ```sh
   cd Cipher_Codes/Diffie-Hellman
   ```
3. Run the script:
   ```sh
   python diffie_hellman.py
   ```

### Running on GitHub Codespaces
1. Open the repository on GitHub.
2. Click on the **Codespaces** tab.
3. Select **New Codespace** to launch an online development environment.
4. Run the script inside the terminal.

## Output
```
prime no.: 23
premitive root: 5
PvA: 6
PvB: 15
Public Key of A:  8
Public Key of B:  19
shared key of A:  2
Shared key of B:  2
Shared key is the same. Key exchange is perfect...
```


