from PIL import Image
import numpy as np

def encrypt_decrypt_image(input_path, output_path, key):
    #load image
    img = Image.open(input_path)
    img_array = np.array(img)

    #encrypt/decrypt using XOR operation
    encrypted_array = img_array ^ key

    #convert back to image and save
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Saved: {output_path}")

#encrypt
encrypt_decrypt_image("original.jpg", " encrypted.jpg", key = 123)

#decrypt
encrypt_decrypt_image("_encrypted.jpg", "decrypted.jpg", key = 123)
