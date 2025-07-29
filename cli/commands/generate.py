import base58
from core.crypto import generate_key_pair
from core.did import create_did_document, save_did_document


def run():
    print("[*] Generating Ed25519 key pair...")
    private_pem, public_pem = generate_key_pair()

    # Konversi public key ke Base58 (DIDKey format umum)
    public_key_base58 = base58.b58encode(public_pem).decode("utf-8")
    did_doc = create_did_document(public_key_base58)

    # Simpan kunci dan dokumen
    with open("private_key.pem", "wb") as f:
        f.write(private_pem)

    with open("public_key.pem", "wb") as f:
        f.write(public_pem)

    did_filename = f'did_weva_{public_key_base58[:16]}.json'
    save_did_document(did_doc, f"./examples/{did_filename}")

    print(f"[+] Key pair generated and saved as private_key.pem / public_key.pem")
    print(f"[+] DID Document saved to ./examples/{did_filename}")
    print(f"[✓] DID: {did_doc['id']}")
