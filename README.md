# 🌐 WEVA ID Core

**Sistem Identitas Digital Desentralisasi**  
Versi: v0.1 — masih tahap awal, proof-of-concept.

---

## 🧭 Visi

Membangun sistem identitas digital yang:

- Tidak dikendalikan otoritas pusat (negara, perusahaan, platform).
- Memberikan kedaulatan penuh pada individu.
- Menggunakan teknologi terbuka (DID, kriptografi, W3C standard).
- Transparan, bisa diaudit, dan open-source.

---

## 🔧 Fitur Utama

- 🔐 Generate keypair dengan Ed25519
- 🆔 Buat DID Document (`did:weva:abc123`)
- ✍️ Tanda tangan data digital
- ✅ Verifikasi tanda tangan
- 📦 Format dokumen sesuai standar W3C DID v1.0

---

## 📁 Struktur Proyek

weva_id_core/
│
├── core/ # Logika inti (DID, crypto, resolver)
│ ├── init.py
│ ├── crypto.py
│ ├── did.py
│ └── resolver.py
│
├── cli/ # Command Line Interface
│ ├── init.py
│ ├── weva.py
│ └── commands/
│ ├── init.py
│ ├── generate.py
│ ├── sign.py
│ └── verify.py
│
├── examples/ # Contoh data DID
│ └── did_sample.json
│
├── docs/ # Dokumentasi dan konsep awal
│ └── konsep.md
│
├── LICENSE # Lisensi MIT
├── CONTRIBUTING.md # Panduan kontribusi
├── ROADMAP.md # Rencana pengembangan
├── requirements.txt # Dependensi Python
└── README.md # Dokumentasi utama proyek 


---

## 🚀 Cara Menjalankan

```bash
# 1. Clone repositori ini
git clone https://github.com/JunW3Weva/weva_id_core.git
cd weva_id_core

# 2. Install dependensi
pip install -r requirements.txt

# 3. Jalankan CLI
python -m cli.weva

🔑 Fitur Utama
🔐 Key generation (berbasis base58 & ed25519)

🆔 DID Document creator

✍️ Digital signature & verifikasi

🧠 Resolver DID lokal

🧪 Siap untuk diintegrasikan dengan MetaMask & QR code

🤝 Kontribusi
Kami sangat terbuka terhadap kontribusi dari siapa pun. Baca CONTRIBUTING.md untuk mengetahui cara kamu bisa ikut serta

🗺️ Roadmap
📌 Lihat rencana pengembangan jangka pendek dan panjang di ROADMAP.md

👤 Founder
Built with ❤️ by Arjuna — Founder of WEVA
