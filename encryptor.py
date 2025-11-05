from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from PIL import Image
import os

class ImageEncryptor:
    @staticmethod
    def encrypt_image(file_path, password):
        """
        Encrypts an image file using AES encryption.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError("Invalid file path.")
        
        img = Image.open(file_path)
        if img.format not in ["PNG", "JPEG", "JPG"]:
            raise ValueError("Unsupported image format. Use PNG or JPEG.")

        with open(file_path, 'rb') as f:
            image_data = f.read()

        key = password.encode()
        if len(key) not in [16, 24, 32]:
            raise ValueError("Password must have minimum 16 characters long containing ateast one special character'!,@,#,$,%,^,&,*' and numericals.")

        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))

        with open(file_path, 'wb') as f:
            f.write(iv)
            f.write(encrypted_data)

    @staticmethod
    def decrypt_image(file_path, password):
        """
        Decrypts an AES-encrypted image file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError("Invalid file path.")

        with open(file_path, 'rb') as f:
            iv = f.read(16)
            encrypted_data = f.read()

        key = password.encode()
        cipher = AES.new(key, AES.MODE_CBC, iv)

        try:
            decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
            with open(file_path, 'wb') as f:
                f.write(decrypted_data)
        except ValueError:
            raise ValueError("Invalid password or corrupted file.")
