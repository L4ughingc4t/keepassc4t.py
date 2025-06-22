from pykeepass import PyKeePass
import sys

if len(sys.argv) != 3:
    print("Usage: python3 kdbx_list_entries.py <file.kdbx> <password>")
    sys.exit(1)

kdbx_file = sys.argv[1]
password = sys.argv[2]

try:
    kp = PyKeePass(kdbx_file, password=password)
    for entry in kp.entries:
        print("Title      :", entry.title)
        print("Username   :", entry.username)
        print("Password   :", entry.password)
        print("URL        :", entry.url)
        print("Notes      :", entry.notes)
        print("-" * 40)
except Exception as e:
    print(f"[!] Error: {e}")
