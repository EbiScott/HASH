# HASH
HASH  is a Linux-based, menu-driven Python tool for **encoding, decoding, hashing, and dictionary-based hash cracking**.  
It is designed for learning, CTFs, and offline password analysis in a legal and ethical environment.

This tool **does not ship wordlists** but instead uses system-installed wordlists (e.g. RockYou, SecLists).

---

## Features

### Encoding
- Hex
- URL encoding
- Base64
- HTML character entities
- UUEncode
- Quoted-Printable

### Decoding
- Hex
- URL decoding
- Base64
- HTML character entities
- UUDecode
- Quoted-Printable

### Hashing
- MD5
- SHA1
- SHA256
- SHA512

### Hash Cracking (Dictionary Attack)
- MD5
- SHA1
- SHA256
- SHA512
- Uses wordlists from `/usr/share/wordlists`
- Graceful interruption with `CTRL+C`

---

## Requirements

- Linux
- Python 3.9+
- Wordlists installed in `/usr/share/wordlists`

Recommended:
- Kali Linux / Parrot OS
- `rockyou.txt`
- `seclists`

---

## Installing Wordlists (if not already installed)

### RockYou
```bash
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
```

## SecLists

```sudo apt install seclists```

## Installation

Clone the repository:
```
git clone https://github.com/EbiScott/HASH.git
cd HaSherr
```

Make sure Python is available:

```python3 --version```

Usage

Run the tool:

```python3 HaSherr.py```


You will be presented with a menu to:

- Encode data

- Decode data

- Generate hashes

- Crack hashes using wordlists


## Wordlists

HASH does not include wordlists.

It expects wordlists to be available in:

`/usr/share/wordlists/`


## Examples used by the tool:

```
/usr/share/wordlists/rockyou.txt

/usr/share/wordlists/seclists/Passwords/
```

You may also provide a custom full path when prompted.

### Notes on Hash Cracking


Hashes are not decoded, they are cracked by comparison

Long runtimes are normal with large wordlists

If no match is found, the password is likely not in the selected wordlist

Use `CTRL+C` to stop cracking


## Disclaimer

This tool is intended for educational purposes only.

Do not use this tool on systems or data you do not own or have explicit permission to test.
The author is not responsible for misuse.

## Made by: X - @Ebi_Scott


