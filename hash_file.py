import hashlib

# -------------------
# Hash functions
# -------------------

def md5_hash(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()

def sha1_hash(data: str) -> str:
    return hashlib.sha1(data.encode()).hexdigest()

def sha256_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def sha512_hash(data: str) -> str:
    return hashlib.sha512(data.encode()).hexdigest()

# -------------------
# Menu
# -------------------

def hash_menu():
    print("""
[1] MD5
[2] SHA1
[3] SHA256
[4] SHA512
[0] Back
""")


    choice = input(">> ").strip()
    if choice == "0":
        return

    data = input("Enter plaintext:\n> ")

    try:
        if choice == "1":
            result = md5_hash(data)
        elif choice == "2":
            result = sha1_hash(data)
        elif choice == "3":
            result = sha256_hash(data)
        elif choice == "4":
            result = sha512_hash(data)
        else:
            print("[!] Invalid option")
            return

        print(f"\n[+] Hash output:\n{result}")

    except Exception as e:
        print(f"[!] Hashing error: {e}")

    input("\nPress Enter to continue...")





