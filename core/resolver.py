import json
import os

def resolve_did(did: str, directory: str = "./examples") -> dict:
    """
    Resolve a DID to its document from a local directory.
    """
    filename = did.replace(":", "_") + ".json"
    filepath = os.path.join(directory, filename)

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"DID document not found: {filepath}")

    with open(filepath, "r") as f:
        return json.load(f)
