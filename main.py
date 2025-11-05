import tkinter as tk
from tkinter import filedialog, messagebox
from encryptor import ImageEncryptor
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Cipher Tool")
        self.root.geometry("600x600")
        
        # Set the background image
        self.set_background_image()

        # Title Label
        tk.Label(root, text="Image Encryption & Decryption", font=("Itlic", 16), bg='black', fg='white').pack(pady=10)

        # File Path Entry
        tk.Label(root, text="Select Image(s):", bg='black', fg='white').pack()
        self.file_path_entry = tk.Entry(root, width=40)
        self.file_path_entry.pack(pady=5)

        # Browse Button
        tk.Button(root, text="Browse", bg='blue', fg='black', command=self.browse_file).pack(pady=5)

        # Password Entry
        tk.Label(root, text="Password:", bg='black', fg='white').pack()
        self.password_entry = tk.Entry(root, show="*", width=30)
        self.password_entry.pack(pady=5)

        # Image Preview Label
        self.image_label = tk.Label(root, text="Preview", bg='black', fg='white')
        self.image_label.pack(pady=5)

        # Buttons for Encryption and Decryption
        tk.Button(root, text="Encrypt", bg='red', fg='black', command=self.encrypt).pack(pady=10)
        tk.Button(root, text="Decrypt", bg='green', fg='black', command=self.decrypt).pack(pady=10)

        # Footer
        tk.Label(root, text="Team 7.", fg="white", bg='black').pack(side="bottom", pady=10)

    def set_background_image(self):
        try:
            background_image = Image.open("background.jpg")  # Ensure this path is correct
            background_image = background_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
            background_image_tk = ImageTk.PhotoImage(background_image)
            background_label = tk.Label(self.root, image=background_image_tk)
            background_label.place(relwidth=1, relheight=1)
            background_label.image = background_image_tk  # Keep a reference to prevent garbage collection
        except FileNotFoundError:
            messagebox.showerror("Error", "Background image not found. Please ensure 'background.jpg' is in the project directory.")
            self.root.quit()  # Exit if background image is missing

    def browse_file(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_paths:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, ', '.join(file_paths))  # Display the selected file paths
            self.preview_image(file_paths[0])  # Preview the first image selected

    def preview_image(self, file_path):
        try:
            img = Image.open(file_path)
            img.thumbnail((250, 250))  # Resize for preview
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk  # Keep a reference to prevent garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load image preview: {str(e)}")

    def encrypt(self):
        file_paths = self.file_path_entry.get().split(", ")
        password = self.password_entry.get()

        if not file_paths or not password:
            messagebox.showerror("Error", "Please select an image and enter a password.")
            return

        try:
            for file_path in file_paths:
                ImageEncryptor.encrypt_image(file_path, password)
            messagebox.showinfo("Success", "Images encrypted successfully!")
            self.password_entry.delete(0, tk.END)  # Clear the password entry after encryption
            
            # Hide the image preview after encryption
            self.image_label.config(image='')
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt(self):
        file_paths = self.file_path_entry.get().split(", ")
        password = self.password_entry.get()

        if not file_paths or not password:
            messagebox.showerror("Error", "Please select an image and enter the password.")
            return

        try:
            for file_path in file_paths:
                ImageEncryptor.decrypt_image(file_path, password)
            messagebox.showinfo("Success", "Images decrypted successfully!")
            self.password_entry.delete(0, tk.END)  # Clear the password entry after decryption
            
            # Re-display the image preview after decryption
            self.preview_image(file_paths[0])  # Preview the first image
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
