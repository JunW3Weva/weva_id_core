import json

def create_did_document(public_key_base58: str) -> dict:
    did = f"did:weva:{public_key_base58[:16]}"
    return {
        "@context": "https://www.w3.org/ns/did/v1",
        "id": did,
        "verificationMethod": [
            {
                "id": f"{did}#key-1",
                "type": "Ed25519VerificationKey2020",
                "controller": did,
                "publicKeyBase58": public_key_base58
            }
        ],
        "authentication": [
            f"{did}#key-1"
        ]
    }

def save_did_document(did_document: dict, filepath: str):
    with open(filepath, 'w') as f:
        json.dump(did_document, f, indent=2)
