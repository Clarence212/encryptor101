# encryptor101

# Educational Ransomware Example (AES Encryption)

⚠️ **Warning: This code is for educational purposes only. It simulates the process of ransomware encryption and should never be run on any system with important data. Use only in controlled, isolated environments such as virtual machines or sandbox environments.**

## Overview
This project demonstrates the basic concept of ransomware by encrypting files using AES (Advanced Encryption Standard) encryption in CBC mode. The code is a proof-of-concept for educational purposes, aiming to help users understand how ransomware operates and how encryption works in cybersecurity.

## Key Features
- Simulates encryption of files using AES-128 encryption.
- Encrypts files inside a specified folder and adds `.encrypted` extension to the encrypted files.
- Implements basic encryption algorithms like CBC (Cipher Block Chaining).
- Encrypts files with a unique encryption key that is saved in a binary file.

## Important Notes
- **This code is intended solely for educational purposes** and should not be used for any malicious activity.
- **Do not run** this code on any system with important or sensitive data.
- It’s designed to be run in a **virtual machine** or a **test environment** only.
- The code deletes the original files after encryption, so **make sure you have backups** before running this on test data.

## Usage
1. Clone or download the repository.
2. Run the script only on test systems or isolated environments.
3. Files inside the designated folder (e.g., `TESTFOLDER`) will be encrypted.
4. The encryption key will be saved as `encryption_key.bin` for later decryption (for educational purposes).

## Disclaimer
This repository is for learning and research purposes only. **By using this code, you agree that you will not use it for malicious purposes** or to harm others' data or systems.

## License
This program is licensed under the Apache 2.0 License.


