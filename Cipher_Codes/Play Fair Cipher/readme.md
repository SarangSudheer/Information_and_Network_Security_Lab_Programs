# Playfair Cipher Implementation

### Playfair Cipher 
- The Playfair cipher is a digraph substitution cipher that encrypts pairs of letters instead of single letters. It was invented by Charles Wheatstone in 1854 but is named after Lord Playfair, who promoted its use.
- It uses a 5x5 matrix of letters derived from a keyword, omitting 'J' or replacing it with 'I'.
- The encryption process follows specific rules depending on the positioning of letter pairs within the matrix.

## Features
- Encrypts messages using the Playfair cipher.
- Handles duplicate letters and odd-length messages by inserting filler characters.
- Uses a keyword to dynamically generate the cipher matrix.

## How to Run the Code

### Run Live
[Click here to Run Live](https://colab.research.google.com/drive/19q2CR3CwSWWNdQCwQ5TNhERBr7WWiK0p?usp=sharing)

### Running Locally
1. Clone the repository:
   ```sh
   gh repo clone SarangSudheer/Information_and_Network_Security_Lab_Programs
   ```
2. Navigate to the directory:
   ```sh
   cd Cipher_Codes/Playfair Cipher
   ```
3. Run the script:
   ```sh
   python play_fair_cipher.py
   ```

### Running on GitHub Codespaces
1. Open the repository on GitHub.
2. Click on the **Codespaces** tab.
3. Select **New Codespace** to launch an online development environment.
4. Run the script inside the terminal.

## Output
```
Enter the message: Hello World
Enter the key: Security
Encrypted: FUOQMPXNSPHQ
```


