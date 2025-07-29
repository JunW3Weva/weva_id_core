# 📖 Konsep Dasar WEVA ID

## Apa itu WEVA?

WEVA adalah sistem identitas digital terdesentralisasi (Decentralized Identity / DID) yang dirancang untuk memberikan **kedaulatan penuh** kepada individu atas data identitas mereka, tanpa bergantung pada otoritas pusat seperti pemerintah, perusahaan besar, atau lembaga tertentu.

## Tujuan Utama

- Mengganti pendekatan tradisional (KTP/NIK) yang terpusat dan rentan kebocoran.
- Menggunakan teknologi open standard (W3C DID, cryptography) untuk memastikan interoperabilitas.
- Mengedukasi publik agar sadar dan mampu mengontrol identitas digital mereka sendiri.

## Masalah yang Ingin Dipecahkan

1. **Kebocoran Data**: NIK dan data KTP sering bocor dan dijual bebas.
2. **Vendor Lock-in**: Identitas digital saat ini dikontrol Google, Facebook, Apple.
3. **Kurangnya Kendali**: Pengguna tidak tahu siapa yang menyimpan, mengakses, dan menjual data mereka.

## Prinsip Desain

- ✅ Desentralisasi teknis dan sosial
- 🔒 Privasi by default
- 🧠 Kesadaran pengguna sebagai fondasi
- 💡 Open-source dan auditabel publik

## Komponen Utama WEVA

| Komponen        | Penjelasan                                                                 |
|----------------|----------------------------------------------------------------------------|
| **DID Document** | File JSON yang berisi public key, metode autentikasi, dsb                 |
| **DID**         | Identifier unik berbentuk `did:weva:xyz123`                               |
| **Ed25519**     | Algoritma kriptografi yang digunakan untuk tanda tangan dan verifikasi    |
| **CLI Tool**    | Alat command-line untuk generate, sign, verify, dan kelola identitas      |

## Contoh Skema

