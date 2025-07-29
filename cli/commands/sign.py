from core.crypto import sign_data


def run():
    print("[*] Membaca private_key.pem...")

    with open("private_key.pem", "rb") as f:
        private_key_pem = f.read()

    message = input("Masukkan pesan yang ingin ditandatangani: ").encode("utf-8")

    signature = sign_data(private_key_pem, message)

    with open("signature.txt", "wb") as f:
        f.write(signature)

    print("[✓] Pesan berhasil ditandatangani.")
    print("[+] Signature disimpan ke signature.txt")
