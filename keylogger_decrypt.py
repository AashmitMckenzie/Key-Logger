from cryptography.fernet import Fernet
import base64
import os

LOG_DIR = r"C:\Aashmit.2\Important\DEPRESSION\CODING\Cyber Security\Key Logger\Texts"
PASSWORD = "Aashmit180869420"

def generate_key(password):
    return Fernet(base64.urlsafe_b64encode(password.ljust(32).encode()[:32]))

def get_latest_encrypted_file():
    files = [f for f in os.listdir(LOG_DIR) if f.endswith(".enc")]
    if not files:
        raise FileNotFoundError("No encrypted files found.")
    return os.path.join(LOG_DIR, max(files, key=lambda f: os.path.getctime(os.path.join(LOG_DIR, f))))

def decrypt_file(filename, password):
    key = generate_key(password)
    
    with open(filename, "rb") as f:
        encrypted_data = f.read()
    
    decrypted_data = key.decrypt(encrypted_data)
    
    decrypted_filename = filename.replace(".enc", "_decrypted.txt")
    
    with open(decrypted_filename, "wb") as f:
        f.write(decrypted_data)
    
    print(f"Decrypted file saved as: {decrypted_filename}")

ENC_FILE = get_latest_encrypted_file()
decrypt_file(ENC_FILE, PASSWORD)
