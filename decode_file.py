import base64
import binascii
import urllib.parse
import html
import quopri

# -------------------
# Decoders
# -------------------

def hex_decode(data: str) -> str:
    return binascii.unhexlify(data).decode()

def url_decode(data: str) -> str:
    return urllib.parse.unquote(data)

def base64_decode(data: str) -> str:
    return base64.b64decode(data).decode()

def html_decode(data: str) -> str:
    return html.unescape(data)

def uu_decode(data: str) -> str:
    return binascii.a2b_uu(data.encode()).decode()

def quoted_printable_decode(data: str) -> str:
    return quopri.decodestring(data.encode()).decode()

# -------------------
# Menu
# -------------------

def decode_menu():
    print("""
[1] Hex
[2] URL
[3] Base64
[4] HTML Character Entities
[5] UUDecode
[6] Quoted-Printable
[0] Back
""")

    choice = input(">> ").strip()
    if choice == "0":
        return

    data = input("Enter encoded string:\n> ")

    try:
        if choice == "1":
            result = hex_decode(data)
        elif choice == "2":
            result = url_decode(data)
        elif choice == "3":
            result = base64_decode(data)
        elif choice == "4":
            result = html_decode(data)
        elif choice == "5":
            result = uu_decode(data)
        elif choice == "6":
            result = quoted_printable_decode(data)
        else:
            print("[!] Invalid option")
            return

        print(f"\n[+] Decoded output:\n{result}")

    except Exception as e:
        print(f"[!] Decode error: {e}")

    input("\nPress Enter to continue...")




