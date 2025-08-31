# Image Encryption & Decryption Tool

A Python-based tool that demonstrates how images can be encrypted and decrypted using two simple cryptographic techniques:
- XOR-based encryption
- Pixel Swapping encryption

This project is designed for learning purposes and helps in understanding how cryptography concepts can be applied to digital images.

---

## Project Structure


📦 IMAGEENCRYPTIIONPROJ
 ┣ 📜 image_encryption.py     # Main Python script (encryption & decryption)
 ┣ 📜 README.md               # Project documentation
 ┣ 📜 swap_key.pkl            # Auto-generated key file for pixel swap decryption
 ┣ 📜 input.jpg               # Sample input image
 ┣ 📜 encrypted.png           # Encrypted image (XOR method)
 ┣ 📜 pixel_swapped.png       # Encrypted image (Pixel Swap method)
 ┣ 📜 decrypted.png           # Decrypted image from XOR
 ┗ 📜 decrypted_swap.png      # Decrypted image from Pixel Swap

---


## 📌 Objectives  
The objective of this project is to implement a basic image encryption and decryption system using Python. It focuses on:

- Exploring how encryption can protect images.
- Implementing XOR-based scrambling and pixel position shuffling.
- Understanding the importance of keys and reversible transformations in cryptography.
- Providing a hands-on learning experience for beginners in cybersecurity and image processing.

---

## 📖 Description  
The project demonstrates two encryption methods:

1️⃣ XOR Encryption / Decryption

- Each pixel’s RGB values are XORed with a secret key (KEY = 50 by default).
- Produces a distorted, encrypted image.
- Running XOR with the same key decrypts the image back to its original form.
- ✅ Strength: Fast and lightweight.
- ⚠️ Limitation: Weak security if the key space is small.

2️⃣ Pixel Swapping Encryption / Decryption

- Pixels are randomly shuffled across the image.
- The shuffle order is stored in a key file (swap_key.pkl).
- Decryption uses this key to restore the image.
- ✅ Strength: Makes the image completely unrecognizable.
- ⚠️ Limitation: Requires secure handling of the shuffle key.  

---
