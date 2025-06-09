from PIL import Image
from tkinter import filedialog, Tk, Button, Label, messagebox
import random
import os

def encrypt_image(input_path, key=123):
    try:
        img = Image.open(input_path)
        pixels = img.load()
        width, height = img.size

        # XOR encryption
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (
                    (r ^ key) % 256,
                    (g ^ key) % 256,
                    (b ^ key) % 256
                )

        # Random pixel swapping
        for _ in range(1000):
            x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
            x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
            pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]

        # Save encrypted image
        base, ext = os.path.splitext(input_path)
        output_path = base + "_encrypted" + ext
        img.save(output_path)

        messagebox.showinfo("✅ Success", f"Encrypted image saved as:\n{output_path}")

    except Exception as e:
        messagebox.showerror("❌ Error", f"An error occurred:\n{e}")

def select_and_encrypt():
    input_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if input_path:
        encrypt_image(input_path, key=123)

def close_app():
    root.destroy()

# Create the root window globally so close_app can access it
root = Tk()
root.title("Image Encryption Tool")
root.geometry("300x150")
root.resizable(False, False)

Label(root, text="Select an image to encrypt:", font=("Arial", 12)).pack(pady=10)
Button(root, text="Select Image", command=select_and_encrypt, width=20).pack(pady=5)
Button(root, text="Exit", command=close_app, width=20).pack(pady=5)

root.mainloop()

