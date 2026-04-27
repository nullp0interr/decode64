from Cryptodome.Cipher import AES
import base64

print("--- aes decryptor ---")

# get key and data
key_input = input("Enter a key (Base64): ")
data_input = input("Enter a encode data (Base64): ")

try:
    key = base64.b64decode(key_input)
    data = base64.b64decode(data_input)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(data).decode('utf-8').strip()
    print(f"\nencoded: {decrypted}")
except ValueError as e:
    print(f"\nerror: uncorrect key or data not match with correct format, details: {e}")
except Exception as e:
    print(f"\nunhandle exception: {e}")
