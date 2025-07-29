import sys

from cli.commands import generate, sign, verify


def print_help():
    print("""
WEVA ID CLI - Perintah yang tersedia:

  generate   → Generate key pair dan DID Document
  sign       → Tanda tangani pesan menggunakan private key
  verify     → Verifikasi tanda tangan dengan public key

Contoh:
  python weva.py generate
  python weva.py sign
  python weva.py verify
""")


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()

    if command == "generate":
        generate.run()
    elif command == "sign":
        sign.run()
    elif command == "verify":
        verify.run()
    else:
        print(f"[!] Perintah tidak dikenal: {command}")
        print_help()


if __name__ == "__main__":
    main()
