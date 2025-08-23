from PIL import Image
import random
import os
import pickle  # to save and load swap order

KEY = 50  # Key for XOR encryption

def xor_encrypt_decrypt(image_path, output_path):
    """Encrypt or decrypt using XOR method."""
    image = Image.open(image_path)
    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ KEY, g ^ KEY, b ^ KEY)

    image.save(output_path)
    print(f"Saved: {output_path}")

def pixel_swap_encrypt(image_path, output_path, key_file):
    """Encrypt using reversible pixel swapping."""
    image = Image.open(image_path)
    pixels = image.load()

    coords = [(x, y) for x in range(image.width) for y in range(image.height)]
    shuffled_coords = coords[:]
    random.shuffle(shuffled_coords)

    # Save shuffle order for decryption
    with open(key_file, "wb") as f:
        pickle.dump(shuffled_coords, f)

    new_image = Image.new(image.mode, image.size)
    new_pixels = new_image.load()

    for (x, y), (nx, ny) in zip(coords, shuffled_coords):
        new_pixels[nx, ny] = pixels[x, y]

    new_image.save(output_path)
    print(f"Saved: {output_path}")
    print(f"Key saved: {key_file}")

def pixel_swap_decrypt(image_path, output_path, key_file):
    """Decrypt pixel swapped image using saved key."""
    if not os.path.exists(key_file):
        print("Key file not found. Cannot decrypt.")
        return

    # Load shuffle order
    with open(key_file, "rb") as f:
        shuffled_coords = pickle.load(f)

    image = Image.open(image_path)
    pixels = image.load()

    coords = [(x, y) for x in range(image.width) for y in range(image.height)]
    new_image = Image.new(image.mode, image.size)
    new_pixels = new_image.load()

    for (x, y), (nx, ny) in zip(coords, shuffled_coords):
        new_pixels[x, y] = pixels[nx, ny]

    new_image.save(output_path)
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    image_name = input("Enter image file name (e.g., input.jpg): ")

    if not os.path.exists(image_name):
        print("File not found! Put the image in the same folder as this script.")
        exit()

    action = input("Encrypt or Decrypt? (e/d): ").lower()
    method = input("Choose method: 1) XOR  2) Pixel Swap: ")

    if action == "e":  # Encrypt
        if method == "1":
            xor_encrypt_decrypt(image_name, "encrypted.png")
        elif method == "2":
            pixel_swap_encrypt(image_name, "pixel_swapped.png", "swap_key.pkl")
        else:
            print("Invalid method choice.")

    elif action == "d":  # Decrypt
        if method == "1":
            xor_encrypt_decrypt(image_name, "decrypted.png")
        elif method == "2":
            pixel_swap_decrypt(image_name, "decrypted_swap.png", "swap_key.pkl")
        else:
            print("Invalid method choice.")

    else:
        print("Invalid action.")
 