# crack_hash.py
import hashlib
import os

WORDLIST_BASE = "/usr/share/wordlists"

WORDLISTS = {
    "1": ("rockyou.txt", "RockYou"),
    "2": ("dirbuster/directory-list-2.3-small.txt", "DirBuster Small"),
    "3": ("dirbuster/directory-list-2.3-medium.txt", "DirBuster Medium"),
    "4": ("dirbuster/directory-list-2.3-big.txt", "DirBuster Big"),
    "5": ("seclists/Passwords/Common-Credentials/10k-most-common.txt", "SecLists Top 10k"),
    "6": ("seclists/Passwords/Common-Credentials/100k-most-common.txt", "SecLists Top 100k"),
    "7": ("custom", "Custom path")
}

# -------------------
# Hash computation
# -------------------

def compute_hash(word: str, algo: str) -> str:
    word_bytes = word.encode()

    match algo:
        case "md5":
            return hashlib.md5(word_bytes).hexdigest()
        case "sha1":
            return hashlib.sha1(word_bytes).hexdigest()
        case "sha256":
            return hashlib.sha256(word_bytes).hexdigest()
        case "sha512":
            return hashlib.sha512(word_bytes).hexdigest()
        case _:
            raise ValueError("Unsupported hash algorithm")

# -------------------
# Wordlist selection
# -------------------

def select_wordlist():
    print("\nSelect wordlist:\n")
    for key, (_, name) in WORDLISTS.items():
        print(f"[{key}] {name}")

    choice = input("\n>> ").strip()

    if choice not in WORDLISTS:
        print("[!] Invalid selection")
        return None

    path, _ = WORDLISTS[choice]

    if path == "custom":
        return input("Enter full path to wordlist:\n> ").strip()

    full_path = os.path.join(WORDLIST_BASE, path)

    if not os.path.exists(full_path):
        print(f"[!] Wordlist not found: {full_path}")
        print("[!] Is it installed on this system?")
        return None

    return full_path

# -------------------
# Cracker
# -------------------

def crack_hash(target_hash: str, algo: str, wordlist_path: str):
    with open(wordlist_path, "r", errors="ignore") as f:
        for count, word in enumerate(f, 1):
            word = word.strip()
            if not word:
                continue

            if compute_hash(word, algo) == target_hash:
                print("\n[+] Hash cracked!")
                print(f"[+] Password: {word}")
                print(f"[+] Attempts: {count}")
                return

            if count % 100000 == 0:
                print(f"[*] Tried {count} passwords...")

    print("\n[-] Hash not found in wordlist")

# -------------------
# Menu
# -------------------

def crack_menu():
    print("""
[1] MD5
[2] SHA1
[3] SHA256
[4] SHA512
[0] Back
""")

    algo_choice = input(">> ").strip()
    if algo_choice == "0":
        return

    algo_map = {
        "1": "md5",
        "2": "sha1",
        "3": "sha256",
        "4": "sha512"
    }

    algo = algo_map.get(algo_choice)
    if not algo:
        print("[!] Invalid option")
        return

    target_hash = input("Enter hash to crack:\n> ").strip().lower()
    wordlist = select_wordlist()

    if not wordlist:
        return

    crack_hash(target_hash, algo, wordlist)
    input("\nPress Enter to continue...")








