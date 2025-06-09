from PIL import Image
import random

# Load image
def load_image(path):
    return Image.open(path)

# Encrypt: XOR each pixel with a key
def xor_encrypt(img, key):
    img = img.convert('RGB')
    encrypted_img = Image.new('RGB', img.size)
    pixels = img.load()
    encrypted_pixels = encrypted_img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            encrypted_pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    return encrypted_img

# Encrypt: Randomly swap pixels using a seed
def pixel_shuffle(img, seed):
    img = img.convert('RGB')
    pixels = list(img.getdata())
    width, height = img.size

    random.seed(seed)
    shuffled_pixels = pixels[:]
    random.shuffle(shuffled_pixels)

    encrypted_img = Image.new('RGB', img.size)
    encrypted_img.putdata(shuffled_pixels)

    return encrypted_img

# Decrypt: Reverse pixel shuffling using same seed
def pixel_unshuffle(img, seed):
    width, height = img.size
    img = img.convert('RGB')
    shuffled_pixels = list(img.getdata())

    random.seed(seed)
    indices = list(range(len(shuffled_pixels)))
    random.shuffle(indices)

    original_pixels = [None] * len(indices)
    for i, idx in enumerate(indices):
        original_pixels[idx] = shuffled_pixels[i]

    decrypted_img = Image.new('RGB', img.size)
    decrypted_img.putdata(original_pixels)
    return decrypted_img

# Save image
def save_image(img, path):
    img.save(path)

# Example usage
if __name__ == "__main__":
    key = 123  # XOR key
    seed = 42  # Shuffle seed

    input_path = "/mnt/data/d7c5e880-3be7-4081-ba71-384da5f10cd3.png"
    img = load_image(input_path)

    xor_img = xor_encrypt(img, key)
    shuffled_img = pixel_shuffle(xor_img, seed)

    save_image(shuffled_img, "/mnt/data/encrypted_image.png")

    # Decryption: Reverse operations
    unshuffled_img = pixel_unshuffle(shuffled_img, seed)
    decrypted_img = xor_encrypt(unshuffled_img, key)  # XOR again with same key

    save_image(decrypted_img, "/mnt/data/decrypted_image.png")
