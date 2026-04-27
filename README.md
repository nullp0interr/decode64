# decode64.py 🔓

A lightweight, interactive Python utility for quick AES decryption in ECB mode. 

Designed for penetration testers and CTF players, this tool allows you to easily decrypt AES-ECB ciphertexts directly from the terminal. It automatically handles Base64 decoding for both the encryption key and the ciphertext, making it perfect for quickly verifying hardcoded credentials or weak cryptographic implementations found during security assessments.

## Features
* **Interactive CLI:** Prompts the user for the key and ciphertext at runtime.
* **Base64 Native:** Automatically decodes Base64 inputs for both keys and data.
* **Error Handling:** Gracefully catches invalid keys, incorrect padding, or malformed Base64 strings.

## Prerequisites

This script requires Python 3 and the `pycryptodomex` library.

You can install the required dependency using pip:
```bash
pip install pycryptodomex
```

## 👨‍💻 Author

Crafted with 🖤 by **[nullp0inter](https://github.com/nullp0interr)**

*Feel free to reach out, open issues, or contribute!*
