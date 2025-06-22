# keepassc4t.py

john + keepass2john は KDBX 3（KeePass v2）形式 のみ対応
KDBX 4の場合

kali
Kali Linux ではグローバルな pip install が制限されているので、仮想環境（venv）を使ってインストール・実行
# 1. 
python3 -m venv ~/venvs/keepassenv

# 2. 
source ~/venvs/keepassenv/bin/activate

# 3. 
pip install pykeepass

python3 keepassc4t.py recovery.kdbx /usr/share/wordlists/rockyou.txt


keepass_list_c4t.pyで取得したパスワードを使用して中身を列挙
python3 kpasslistc4t.py recovery.kdbx {password}


一括
expkeepassc4t.py

python3 expkeepassc4t.py recovery.kdbx rockyou.txt
