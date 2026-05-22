import os
try:
    from cryptography.fernet import Fernet
except ImportError:
    print("Error: 'cryptography' library nahi mili. Isey install karne ke liye run karein: pip install cryptography")
    exit()

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("\n[+] Nayi Secret Key kamyabi se 'secret.key' file mein save ho gayi hai!")

def load_key():
    if not os.path.exists("secret.key"):
        print("\n[-] Error: 'secret.key' file nahi mili! Pehle Option 1 select karke key banayein.")
        return None
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    if not key:
        return
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    print("\n" + "="*40)
    print("[🛡️ NEXUS SECURE DATA]:")
    print(encrypted_message.decode())
    print("="*40)
    print("\n[!] Is secure code ko copy karke save kar lein.")

def decrypt_message(encrypted_message):
    key = load_key()
    if not key:
        return
    f = Fernet(key)
    try:
        decrypted_message = f.decrypt(encrypted_message.encode())
        print("\n" + "="*40)
        print("[🔓 UNLOCKED DATA]:")
        print(decrypted_message.decode())
        print("="*40)
    except Exception:
        print("\n[-] Error: Galt chabi (Key) ya kharab encrypted data! Unlock nahi ho sakta.")

if __name__ == "__main__":
    print("="*50)
    print("      NEXUS AUTOMATION AGENCY - SECURE VAULT v1.0      ")
    print("="*50)
    while True:
        print("\n1. Nayi Encryption Key Banayein (Generate Key)")
        print("2. Data ko Lock Karein (Encrypt Data)")
        print("3. Data ko Unlock Karein (Decrypt Data)")
        print("4. Exit")
        choice = input("\nApna Option select karein (1-4): ")
        if choice == '1':
            generate_key()
        elif choice == '2':
            msg = input("Woh sensitive data likhein jise secure karna hai: ")
            encrypt_message(msg)
        elif choice == '3':
            enc_msg = input("Woh encrypted secure code paste karein jise unlock karna hai: ")
            decrypt_message(enc_msg)
        elif choice == '4':
            print("\nNexus Secure Vault band ho raha hai. Stay Safe!")
            break
        else:
            print("\nGalt option! Dubara koshish karein.")
