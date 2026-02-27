import tkinter as tk
from tkinter import filedialog, messagebox
from encryptor import ImageEncryptor
from PIL import Image, ImageTk
import os
import threading

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Photo Cipher Tool - AES Encryption")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.set_background_image()
        self.main_frame = tk.Frame(root, bg='black', bd=2)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        tk.Label(self.main_frame, text="🔐 Image Encryption & Decryption", font=("Arial", 16, "bold"), bg='black', fg='#00FF00').pack(pady=15)
        tk.Label(self.main_frame, text="Secure your images with AES-256 encryption", font=("Arial", 10), bg='black', fg='white').pack()
        tk.Label(self.main_frame, text="📁 Select Image(s):", bg='black', fg='white', font=("Arial", 10, "bold")).pack(pady=(15, 5))
        self.file_path_entry = tk.Entry(self.main_frame, width=40, font=("Arial", 9))
        self.file_path_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Browse", bg='#0066CC', fg='white', command=self.browse_file, font=("Arial", 10, "bold"), relief=tk.RAISED, bd=2, width=15).pack(pady=5)
        tk.Label(self.main_frame, text="🔑 Password:", bg='black', fg='white', font=("Arial", 10, "bold")).pack(pady=(15, 5))
        self.password_entry = tk.Entry(self.main_frame, show="●", width=30, font=("Arial", 10))
        self.password_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Minimum 8 characters recommended for security", font=("Arial", 8, "italic"), bg='black', fg='#CCCCCC').pack()
        self.image_label = tk.Label(self.main_frame, text="Preview", bg='#333333', fg='white', width=35, height=12, relief=tk.SUNKEN)
        self.image_label.pack(pady=15)
        button_frame = tk.Frame(self.main_frame, bg='black')
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="🔒 Encrypt", bg='#FF3333', fg='white', command=self.encrypt, font=("Arial", 11, "bold"), relief=tk.RAISED, bd=2, width=14, padx=5).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="🔓 Decrypt", bg='#33AA33', fg='white', command=self.decrypt, font=("Arial", 11, "bold"), relief=tk.RAISED, bd=2, width=14, padx=5).pack(side=tk.LEFT, padx=5)
        self.status_label = tk.Label(self.main_frame, text="Ready", bg='black', fg='#FFFF00', font=("Arial", 9))
        self.status_label.pack(pady=5)
        tk.Label(self.main_frame, text="Secure Image Encryption Tool", fg="white", bg='black', font=("Arial", 8)).pack(side="bottom", pady=10)

    def set_background_image(self):
        try:
            if os.path.exists("background.jpg"):
                background_image = Image.open("background.jpg")
                background_image = background_image.resize((600, 700), Image.Resampling.LANCZOS)
                background_image_tk = ImageTk.PhotoImage(background_image)
                background_label = tk.Label(self.root, image=background_image_tk)
                background_label.place(relwidth=1, relheight=1)
                background_label.image = background_image_tk
            else:
                self.root.config(bg='#1a1a1a')
        except Exception as e:
            self.root.config(bg='#1a1a1a')

    def browse_file(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp"), ("All Files", "*.*")])
        if file_paths:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, ', '.join(file_paths))
            self.preview_image(file_paths[0])
            self.update_status(f"Selected {len(file_paths)} file(s)")

    def preview_image(self, file_path):
        try:
            img = Image.open(file_path)
            img.thumbnail((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk, text="")
            self.image_label.image = img_tk
        except Exception as e:
            self.update_status(f"Preview error: {str(e)}")

    def update_status(self, message):
        self.status_label.config(text=message)
        self.root.update()

    def encrypt(self):
        file_paths_str = self.file_path_entry.get().strip()
        password = self.password_entry.get()
        if not file_paths_str or not password:
            messagebox.showerror("Error", "Please select an image and enter a password.")
            return
        file_paths = [fp.strip() for fp in file_paths_str.split(",") if fp.strip()]
        if len(password) < 8:
            messagebox.showwarning("Weak Password", "Password should be at least 8 characters for better security.")
            return
        thread = threading.Thread(target=self._encrypt_thread, args=(file_paths, password))
        thread.daemon = True
        thread.start()

    def _encrypt_thread(self, file_paths, password):
        try:
            self.update_status("Encrypting...")
            for i, file_path in enumerate(file_paths):
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"File not found: {file_path}")
                ImageEncryptor.encrypt_image(file_path, password)
            self.update_status("Encryption completed!")
            messagebox.showinfo("Success", f"Successfully encrypted {len(file_paths)} image(s)!")
            self.password_entry.delete(0, tk.END)
            self.image_label.config(image='', text="Preview")
        except Exception as e:
            self.update_status("Encryption failed!")
            messagebox.showerror("Encryption Error", str(e))

    def decrypt(self):
        file_paths_str = self.file_path_entry.get().strip()
        password = self.password_entry.get()
        if not file_paths_str or not password:
            messagebox.showerror("Error", "Please select an image and enter the password.")
            return
        file_paths = [fp.strip() for fp in file_paths_str.split(",") if fp.strip()]
        thread = threading.Thread(target=self._decrypt_thread, args=(file_paths, password))
        thread.daemon = True
        thread.start()

    def _decrypt_thread(self, file_paths, password):
        try:
            self.update_status("Decrypting...")
            for file_path in file_paths:
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"File not found: {file_path}")
                ImageEncryptor.decrypt_image(file_path, password)
            self.update_status("Decryption completed!")
            messagebox.showinfo("Success", f"Successfully decrypted {len(file_paths)} image(s)!")
            self.password_entry.delete(0, tk.END)
            if file_paths:
                self.preview_image(file_paths[0])
        except Exception as e:
            self.update_status("Decryption failed!")
            messagebox.showerror("Decryption Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()