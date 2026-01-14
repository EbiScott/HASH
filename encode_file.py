import base64
import binascii
import urllib.parse
import html
import quopri

# -------------------
# Encoders
# -------------------

def hex_encode(data: str) -> str:
    return binascii.hexlify(data.encode()).decode()

def url_encode(data: str) -> str:
    return urllib.parse.quote(data)

def base64_encode(data: str) -> str:
    return base64.b64encode(data.encode()).decode()

def html_encode(data: str) -> str:
    return html.escape(data)

def uu_encode(data: str) -> str:
    return binascii.b2a_uu(data.encode()).decode().strip()

def quoted_printable_encode(data: str) -> str:
    return quopri.encodestring(data.encode()).decode()

# -------------------
# Menu
# -------------------

def encode_menu():
    print("""
[1] Hex
[2] URL
[3] Base64
[4] HTML Character Entities
[5] UUEncode
[6] Quoted-Printable
[0] Back
""")

    choice = input(">> ").strip()
    if choice == "0":
        return

    data = input("Enter plaintext:\n> ")

    try:
        if choice == "1":
            result = hex_encode(data)
        elif choice == "2":
            result = url_encode(data)
        elif choice == "3":
            result = base64_encode(data)
        elif choice == "4":
            result = html_encode(data)
        elif choice == "5":
            result = uu_encode(data)
        elif choice == "6":
            result = quoted_printable_encode(data)
        else:
            print("[!] Invalid option")
            return

        print(f"\n[+] Encoded output:\n{result}")

    except Exception as e:
        print(f"[!] Encoding error: {e}")

    input("\nPress Enter to continue...")





