# Product Requirements Document (PRD)
**Product Name:** Sistem Transparansi Dana Sosial IPNU-IPPNU (Hybrid App)
**Version:** 2.0 (Hybrid Architecture Update)

## 1. Latar Belakang & Masalah
Pengelolaan dana operasional organisasi IPNU-IPPNU Ranting Desa Gajah saat ini rentan terhadap isu transparansi, manipulasi data kas, dan pencairan dana sepihak. Laporan berbasis pembukuan konvensional atau *database* terpusat (Web2 murni) tidak memiliki *audit trail* yang kuat secara kriptografi.

## 2. Visi Produk
Membangun ekosistem tata kelola keuangan organisasi yang *trustless* (mengeliminasi kebutuhan saling percaya secara buta) melalui pendekatan *Hybrid Architecture*. Sistem ini menggabungkan kecepatan akses informasi publik (Web2) dengan jaminan keamanan finansial yang *immutable* secara desentralisasi (Web3).

## 3. Fitur Utama (Key Features)
1. **Public Immutable Ledger (Web2):** Antarmuka publik yang instan tanpa *login* bagi anggota/kader untuk memantau arus kas secara *real-time*.
2. **Two-Layer Authentication (Hybrid Security):** Pengurus wajib melewati *login server* (Web2) dan menghubungkan kunci privat dompet digital (Web3/MetaMask) sebelum melakukan aksi finansial.
3. **3-of-3 Multi-Signature Protocol:** Dana kas hanya dapat dieksekusi (cair) jika dan hanya jika terdapat tanda tangan digital persetujuan dari tiga pengurus inti (Ketua, Wakil Ketua, dan Bendahara).
4. **Asynchronous WhatsApp Notification:** Notifikasi pencairan dana kas secara otomatis ke WhatsApp pengurus setelah sistem *backend* mendeteksi *event log* dari *blockchain*.

## 4. Target Pengguna (Actors)
* **Anggota (Base Actor):** Warga Desa / Kader IPNU-IPPNU.
* **Pengurus (Sub-Actor):** Bendahara, Wakil Ketua, Ketua (memiliki hak waris/inheritance dari Base Actor + otoritas manajerial).