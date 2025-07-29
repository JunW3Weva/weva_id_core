from core.crypto import verify_signature


def run():
    print("[*] Membaca public_key.pem dan signature.txt...")

    with open("public_key.pem", "rb") as f:
        public_key_pem = f.read()

    with open("signature.txt", "rb") as f:
        signature = f.read()

    message = input("Masukkan pesan yang ingin diverifikasi: ").encode("utf-8")

    valid = verify_signature(public_key_pem, message, signature)

    if valid:
        print("[✓] Signature valid. Pesan tidak dimanipulasi.")
    else:
        print("[✗] Signature TIDAK valid. Pesan mungkin telah dimodifikasi.")
