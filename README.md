# AES Photocipher Tool

## Overview
The AES Photocipher Tool is a software application that employs Advanced Encryption Standard (AES) for robust encryption and decryption of photographs. This tool is designed for users seeking a professional solution to secure their image data.

## Installation Instructions
To install the AES Photocipher Tool, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DHANUSH007sa/AES-Photocipher-tool.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd AES-Photocipher-tool
   ```
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Guide
To use the AES Photocipher Tool, follow these instructions:

1. **Run the application**:
   ```bash
   python main.py
   ```
2. **Encrypt a photograph**:
   - Select the 'Encrypt' option.
   - Choose an image file you wish to encrypt.
   - Enter a secure key (ensure to remember this key for decryption).
   - The encrypted image will be saved in the output directory.

3. **Decrypt a photograph**:
   - Select the 'Decrypt' option.
   - Choose the encrypted image file.
   - Enter the key you used for encryption.
   - The decrypted image will be saved in the output directory.

## Troubleshooting
If you encounter issues, consider the following:

- **Problem: Application fails to start**  
  *Solution: Check if all dependencies are installed correctly. Ensure you're using a supported Python version.*

- **Problem: Decryption fails**  
  *Solution: Ensure you are using the correct key for decryption. Double-check the file you are trying to decrypt.*

## FAQ

**Q: What is AES?**  
A: AES (Advanced Encryption Standard) is a symmetric encryption algorithm widely used across various applications for securing data.

**Q: Is it safe to use this tool?**  
A: Yes, as long as you keep your encryption key secure and private.

**Q: Can I contribute to this project?**  
A: Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
