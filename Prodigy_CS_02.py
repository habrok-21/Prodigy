
try:
    from PIL import Image
except ImportError:
    print("❌ Pillow library not found. Please install it using:")
    print("   pip install pillow")
    exit()

def process_image(input_path, output_path, key):
    """
    Encrypts or decrypts an image using XOR operation.
    Encryption and decryption are identical with XOR.
    """
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):  # Width
        for j in range(img.size[1]):  # Height
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)  # XOR each channel

    img.save(output_path)
    print(f"✅ Processed image saved as {output_path}")

# Example usage:
# Encrypt
# process_image("original.jpg", "encrypted.png", 123)

# Decrypt (same function & key)
# process_image("encrypted.png", "decrypted.png", 123)

if __name__ == "__main__":
    print("\n🖼 Image Encryption Tool (XOR Method)")
    mode = input("Type 'encrypt' or 'decrypt': ").strip().lower()
    in_file = input("Enter input image path: ").strip()
    out_file = input("Enter output image path: ").strip()
    key = int(input("Enter numeric key (0-255): "))

    process_image(in_file, out_file, key)

