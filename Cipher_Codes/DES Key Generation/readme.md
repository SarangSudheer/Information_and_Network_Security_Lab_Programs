# DES Key Generation Implementation

## Description
This program implements a simple DES-like key generation technique. It takes an input string, converts it into binary, applies bitwise operations and shifting techniques, and generates multiple keys with random modifications.

## Features
- Converts input text into binary representation.
- Performs bitwise shifting operations.
- Generates 8 different keys based on shifting and random bit removal.
- Adds complexity to key generation through randomness.

## How to Run the Code

### Run Live
[Click here to Run Live](https://colab.research.google.com/drive/1pCfddGe9et4ucZ1HjiKnQAaVYNSxrl9P?usp=sharing) 

### Running Locally
1. Clone the repository:
   ```sh
   gh repo clone SarangSudheer/Information_and_Network_Security_Lab_Programs
   ```
2. Navigate to the directory:
   ```sh
   cd Cipher_Codes/DES Key Generation
   ```
3. Run the script:
   ```sh
   python des_keygen.py
   ```

### Running on GitHub Codespaces
1. Open the repository on GitHub.
2. Click on the **Codespaces** tab.
3. Select **New Codespace** to launch an online development environment.
4. Run the script inside the terminal.

## Output Example
```
Enter a string : Hello World
Key 1 = 10111110111111010111101100100001011001011101100110110011011101000
Key 2 = 01111011111110010110110110100001000110101110100111100110111010000
Key 3 = 11101111110010110110011000000000110010110110011011001011101000000
Key 4 = 11011111101010100110100000000011000110110011010011011110100000000
Key 5 = 01011110111111100101101100100100001000100101111001101011011110100
Key 6 = 10111111100101101001100000000000110011110110011011001101110100000
Key 7 = 11110111111100101011011001000000011001011110110110011011101000000
Key 8 = 01111111010111100110010000000000010111001101100110111101000000000
```

## Notes
- The script removes the first bit from each byte of the input before processing.
- It applies predefined bitwise left shifts to split parts of the binary string.
- Random bit removal ensures variation in generated keys.
- This is not a full DES key generation but demonstrates a custom key derivation process inspired by DES principles.

