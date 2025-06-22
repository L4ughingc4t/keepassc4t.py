# pykpassc4t.py

john + keepass2john は KDBX 3（KeePass v2）形式 のみ対応
KDBX 4の場合

kali

# 1. 
python3 -m venv ~/venvs/keepassenv

# 2. 
source ~/venvs/keepassenv/bin/activate

# 3. 
pip install pykeepass

python3 keepassc4t.py recovery.kdbx /usr/share/wordlists/rockyou.txt
