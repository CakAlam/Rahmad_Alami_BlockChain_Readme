# Use Case Specification: Sistem Transparansi Dana IPNU-IPPNU (Hybrid App)

## 1. Daftar Aktor dan Pewarisan (Inheritance)
*   **Anggota (Kader/Warga):** Merupakan *base actor* di ranah publik. Aktor ini berinteraksi tanpa autentikasi untuk memastikan asas transparansi informasi tercapai.
*   **Pengurus (Bendahara, Ketua, Wakil Ketua):** Merupakan *sub-actor* yang memiliki otoritas tata kelola. Melalui relasi *generalization*, Pengurus secara otomatis mewarisi seluruh kapabilitas aktor Anggota, ditambah akses ke fitur internal melalui dua lapis autentikasi.

## 2. Lapisan Manajemen Konten (Web2 - Sisi Publik & Autentikasi Awal)
*   **UC-01: Melihat Laporan Kas Real-time**
    *   *Aktor:* Anggota
    *   *Deskripsi:* Menampilkan riwayat uang masuk dan keluar secara instan.
*   **UC-02: Verifikasi Bukti Transaksi On-Chain**
    *   *Relasi:* `<<extend>>` ke UC-01
    *   *Deskripsi:* Fungsi opsional (perluasan) bagi pengunjung untuk melacak dan memverifikasi detail *hash* transaksi langsung ke *blockchain*.
*   **UC-03: Login Akun Pengurus (Web2)**
    *   *Aktor:* Pengurus
    *   *Deskripsi:* Gerbang autentikasi awal berbasis *server* Web2 untuk memvalidasi hak akses ke menu administrasi.

## 3. Lapisan Interaksi Finansial Terdesentralisasi (Web3 - Sisi Internal)
*   **UC-04: Melihat Connect Wallet Web3 (MetaMask)**
    *   *Aktor:* Pengurus
    *   *Deskripsi:* Autentikasi lapis kedua menggunakan *private key* dompet digital untuk eksekusi dana *immutable*.
*   **UC-05: Mencatat Iuran & Pemasukan Kas**
    *   *Aktor:* Bendahara
    *   *Relasi:* `<<include>>` UC-03, `<<include>>` UC-04
*   **UC-06: Mengajukan Proposal Pengeluaran**
    *   *Aktor:* Bendahara
    *   *Relasi:* `<<include>>` UC-03, `<<include>>` UC-04
    *   *Deskripsi:* Membuat draf pengajuan; dana akan terkunci dengan status *Pending* hingga disetujui.
*   **UC-07: Persetujuan Multi Signature (Signing)**
    *   *Aktor:* Ketua, Wakil Ketua, Bendahara
    *   *Relasi:* `<<include>>` UC-03, `<<include>>` UC-04, memicu `<<include>>` UC-08
    *   *Deskripsi:* Penandatanganan kolektif (konsensus 3-of-3).
*   **UC-08: Eksekusi Pencairan Dana via Smart Contract**
    *   *Relasi:* Memicu `<<include>>` UC-09
    *   *Deskripsi:* Proses transfer saldo kas langsung ke alamat tujuan secara desentralisasi jika ambang batas UC-07 terpenuhi.
*   **UC-09: Kirim Notifikasi WhatsApp Otomatis (Python)**
    *   *Deskripsi:* Berjalan asinkronus. *Backend* menangkap *event emission* dari *smart contract* pasca-eksekusi dan mengirimkan laporan WA ke nomor pengurus.