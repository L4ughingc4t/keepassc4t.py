from pykeepass import PyKeePass
import sys

def title_to_username(title):
    return title.lower().replace(' ', '.').replace(',', '').replace('-', '.')

if len(sys.argv) != 4:
    print("Usage: python3 make_cme_user_pass_lists.py <file.kdbx> <password> <output_prefix>")
    sys.exit(1)

kdbx_file = sys.argv[1]
password = sys.argv[2]
out_prefix = sys.argv[3]

kp = PyKeePass(kdbx_file, password=password)

users = set()
passwords = set()

for entry in kp.entries:
    if entry.password:
        user = entry.username if entry.username else title_to_username(entry.title)
        users.add(user)
        passwords.add(entry.password)

with open(f"{out_prefix}_users.txt", "w") as f_users:
    for u in sorted(users):
        f_users.write(u + "\n")

with open(f"{out_prefix}_passwords.txt", "w") as f_pass:
    for p in sorted(passwords):
        f_pass.write(p + "\n")

print(f"[+] Generated {out_prefix}_users.txt and {out_prefix}_passwords.txt")
