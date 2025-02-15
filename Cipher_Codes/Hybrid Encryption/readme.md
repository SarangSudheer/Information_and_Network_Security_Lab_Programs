# Hybrid Encryption System

## 📋 Table of Contents
- [Introduction](#introduction)
- [Design and Implementation of Hybrid Cipher](#design-and-implementation-of-hybrid-cipher)
  - [Design Goals](#design-goals)
  - [Steps in Design](#steps-in-design)
- [Why Hybrid Encryption is Better](#why-hybrid-encryption-is-better)
  - [Resistance to Cryptanalysis Attacks](#resistance-to-cryptanalysis-attacks)
  - [Computational Complexity](#computational-complexity)
  - [Weaknesses](#weaknesses)
  - [Overall Security Benefits](#overall-security-benefits)
- [Mathematical Formulation of Hybrid System](#mathematical-formulation-of-hybrid-system)
  - [AES Encryption (Substitution)](#aes-encryption-substitution)
  - [Transposition (Random Permutation)](#transposition-random-permutation)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
- [How to Run](#how-to-run)
  - [Running Locally](#running-locally)
  - [Running on GitHub Codespaces](#running-on-github-codespaces)
- [Conclusion](#conclusion)

## Introduction
In today's digital age, keeping sensitive information safe is a big challenge. This project explores a hybrid encryption approach that combines **AES (Advanced Encryption Standard)** and a **transposition cipher** to enhance security. AES is a widely used symmetric encryption method that converts readable text into encrypted blocks, ensuring confusion. However, attackers can sometimes detect encrypted patterns. To counter this, we introduce a **transposition step**, which rearranges the encrypted data using a secret rule, further strengthening security.

## Design and Implementation of Hybrid Cipher

### Design Goals
- Ensure **at least 128-bit encryption** strength.
- Use **AES-128 for substitution** and **random permutation for transposition**.
- Resist **frequency and statistical attacks**.
- Eliminate classical cipher weaknesses like pattern recognition.

### Steps in Design
1. **Key Generation**
   - **AES Key:** 128-bit secret key.
   - **Permutation Key:** Secure random permutation for transposition.
2. **Substitution using AES-128**
   - Encrypts plaintext in **16-byte blocks**.
   - Uses an **S-box** for substitution.
   - Padding ensures a **multiple of 16 bytes**.
3. **Transposition (Permutation)**
   - **Random permutation** shuffles the AES ciphertext, preventing pattern recognition.
4. **Cipher Generation**
   - The final **shuffled ciphertext** is obtained.
5. **Decryption**
   - Reverse the transposition to retrieve AES ciphertext.
   - **Decrypt using AES-128 key**.
   - Remove any padding.

## Why Hybrid Encryption is Better

### Resistance to Cryptanalysis Attacks
- **Brute Force:** AES-128 has a **128-bit key**, requiring `2¹²⁸` operations to break.
- **Frequency Analysis:**
  - AES uses a **non-linear S-box**, ensuring strong confusion.
  - The additional **random permutation** further obscures frequency patterns.
- **Chosen Plaintext & Chosen Ciphertext Attacks:**
  - AES resists these attacks due to **key expansion and round transformations**.
  - The transposition step doesn’t expose the key, maintaining security.

### Computational Complexity
- **AES Complexity:**
  - 10 transformation rounds for 128-bit encryption.
  - Steps include **byte substitution (S-box), row shifting, column mixing, and key addition**.
- **Transposition Complexity:**
  - Lightweight but adds an extra **diffusion layer**.

### Weaknesses
- **Permutation Key Management:** A weak permutation can reduce security.
- **Computational Overhead:** Additional transposition increases processing time.
- **Side-Channel Attacks:** AES implementations must resist **timing and power analysis attacks**.

### Overall Security Benefits
- **Combines confusion (AES-128) and diffusion (permutation)** for superior security.
- **More resilient to cryptanalysis** compared to individual ciphers.
- **Increases attack complexity**, making decryption computationally expensive.

## Mathematical Formulation of Hybrid System

### AES Encryption (Substitution)
AES operates on **128-bit blocks** using a secret key and applies multiple transformations.

- **Substitution (S-box):** Each byte is replaced using a **16×16 S-box table**.
- **Permutation (Shift Row):** Row-wise **byte shifting** enhances diffusion.
- **Key Mixing:** Bitwise **XOR** operation between data and round keys.

### Transposition (Random Permutation)
- Permutation is defined by a **randomly generated pattern**.
- Given data sequence `D = (d₁, d₂, ..., dₙ)`,
  - The permutation `π = (p₁, p₂, ..., pₙ)` reorders it as:
    - `T(D) = (dₚ₁, dₚ₂, ..., dₚₙ)`

## Setup and Installation

### Prerequisites
Ensure you have the following installed:
- **Python** (3.8 or later) for Python-based ciphers.
- **Git** for cloning the repository.

### Clone the Repository
Run the following commands to clone and set up the project on your local machine:
```bash
gh repo clone SarangSudheer/Information_and_Network_Security_Lab_Programs
cd Cipher_Codes/Hybrid Encryption
```

## How to Run
Read the steps given in detail below ...

### Running Locally
#### Python Programs:
  Execute the program:
   ```bash
   python hybrid.py
   ```

### Running on GitHub Codespaces
1. Open the repository in GitHub and click on the **Code** button.
2. Select **Create Codespace on Main**.
3. Once the Codespace is ready, open the terminal and navigate to the desired cipher folder.
4. Follow the [Running Locally](#running-locally) steps for Python programs.

## Conclusion
This hybrid cipher leverages **AES-128** for confusion and **random permutation** for diffusion, eliminating recognizable patterns and preventing cryptanalysis attacks.

By combining these two techniques, the hybrid encryption ensures **higher security than individual ciphers** while maintaining efficiency. It is a **strong encryption strategy** for protecting sensitive data against modern cryptographic threats.

