from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature


def generate_key_pair():
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_bytes, public_bytes


def sign_data(private_key_pem, data: bytes):
    private_key = serialization.load_pem_private_key(
        private_key_pem,
        password=None
    )
    signature = private_key.sign(data)
    return signature


def verify_signature(public_key_pem, data: bytes, signature: bytes):
    public_key = serialization.load_pem_public_key(public_key_pem)
    try:
        public_key.verify(signature, data)
        return True
    except InvalidSignature:
        return False
