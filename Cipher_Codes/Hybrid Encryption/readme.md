<!DOCTYPE html>
<html>
<head>
    <title>Hybrid Encryption System</title>
</head>
<body>
    <h1>Hybrid Encryption System</h1>
    
    <h2>Introduction</h2>
    <p>In today's digital age, keeping sensitive information safe is a big challenge. This project explores a hybrid encryption approach that combines <strong>AES (Advanced Encryption Standard)</strong> and a <strong>transposition cipher</strong> to enhance security. AES is a widely used symmetric encryption method that converts readable text into encrypted blocks, ensuring confusion. However, attackers can sometimes detect encrypted patterns. To counter this, we introduce a <strong>transposition step</strong>, which rearranges the encrypted data using a secret rule, further strengthening security.</p>
    
    <h2>Cipher Computational Complexity and Cryptanalysis</h2>
    
    <h3>Hill Cipher</h3>
    <p>Hill Cipher is a matrix-based substitution cipher using matrix multiplication and inversion for encryption and decryption.</p>
    <ul>
        <li><strong>Encryption:</strong> Uses matrix multiplication for substitution.</li>
        <li><strong>Decryption:</strong> Requires matrix inversion, making it computationally complex.</li>
        <li><strong>Cryptanalysis:</strong> Uses known plaintext attack to derive key matrix.</li>
    </ul>
    
    <h3>Playfair Cipher</h3>
    <p>A digraph substitution cipher that processes two characters at a time.</p>
    <ul>
        <li><strong>Encryption:</strong> Uses a 5×5 key matrix.</li>
        <li><strong>Decryption:</strong> Reverse lookup in the matrix.</li>
        <li><strong>Cryptanalysis:</strong> Based on digraph frequency analysis.</li>
    </ul>
    
    <h3>Vigenère Cipher</h3>
    <p>A polyalphabetic substitution cipher using cyclic shifting keys.</p>
    <ul>
        <li><strong>Encryption:</strong> Uses a shifting key applied cyclically.</li>
        <li><strong>Decryption:</strong> Reverse shifting using the same key.</li>
        <li><strong>Cryptanalysis:</strong> Uses Kasiski Examination to break repeated key patterns.</li>
    </ul>
    
    <h2>Design and Implementation of Hybrid Cipher</h2>
    <h3>Design Goals</h3>
    <ul>
        <li>Ensure at least 128-bit encryption strength.</li>
        <li>Combine AES-128 (substitution) with columnar transposition.</li>
        <li>Resist frequency and statistical attacks.</li>
    </ul>
    
    <h3>Encryption and Decryption Process</h3>
    <ol>
        <li>Generate an AES-128 key and a random permutation key.</li>
        <li>Encrypt plaintext using AES-128.</li>
        <li>Apply transposition on AES ciphertext.</li>
        <li>For decryption, reverse the transposition and then decrypt using AES.</li>
    </ol>
    
    <h2>Why Hybrid Encryption is Better</h2>
    <h3>Resistance to Attacks</h3>
    <ul>
        <li><strong>Brute Force:</strong> AES-128 has a 128-bit key, requiring 2^128 operations to break.</li>
        <li><strong>Frequency Analysis:</strong> AES's S-box ensures confusion, further enhanced by random permutation.</li>
        <li><strong>Chosen Plaintext & Ciphertext Attacks:</strong> AES’s key expansion and transformations make it resistant.</li>
    </ul>
    
    <h3>Computational Complexity</h3>
    <p>AES complexity involves 10 transformation rounds per 128-bit block, whereas transposition adds minimal computational overhead but significantly enhances security.</p>
    
    <h3>Weaknesses</h3>
    <ul>
        <li><strong>Key Management:</strong> Poor permutation selection may reduce security.</li>
        <li><strong>Computational Overhead:</strong> Additional steps increase processing time.</li>
    </ul>
    
    <h2>Mathematical Formulation of Hybrid System</h2>
    <h3>AES Encryption (Substitution)</h3>
    <p>AES operates on 128-bit blocks using a secret key and applies multiple transformations, including substitution (S-box), permutation (Shift Rows), and key mixing (XOR operation).</p>
    
    <h3>Transposition (Random Permutation)</h3>
    <p>Permutation is defined by a randomly generated pattern.</p>
    <p><strong>Formula:</strong> T(D) = (dₚ₁, dₚ₂, ..., dₚₙ)</p>
    
    <h2>Conclusion</h2>
    <p>The hybrid cipher leverages AES-128 for confusion and random permutation for diffusion, ensuring superior security. It eliminates recognizable patterns, prevents cryptanalysis attacks, and is an effective strategy against modern cryptographic threats.</p>
</body>
</html>

