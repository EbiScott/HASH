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

## Made by: X - @Ebi_Scott


