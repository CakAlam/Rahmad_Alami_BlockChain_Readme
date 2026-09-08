# User Stories: Sistem Transparansi Dana IPNU-IPPNU (Hybrid App)

## Epic 1: Akses Publik & Transparansi (Sisi Web2)
*   Sebagai **Anggota**, saya ingin **melihat tabel laporan kas secara instan di halaman utama** sehingga **saya mengetahui kondisi keuangan organisasi tanpa perlu login.**
*   Sebagai **Anggota**, saya ingin **melihat detail *hash* transaksi di setiap baris laporan** sehingga **saya bisa memverifikasi keaslian data langsung ke *blockchain* jika diperlukan.**

## Epic 2: Autentikasi Lapis Ganda (Hybrid Security)
*   Sebagai **Pengurus**, saya ingin **melewati proses login berbasis *server* (Web2)** sehingga **saya mendapatkan akses dasar ke menu administrasi internal.**
*   Sebagai **Pengurus**, saya ingin **menghubungkan dompet digital MetaMask (Web3)** sehingga **saya bisa menggunakan *private key* untuk mengotorisasi transaksi finansial.**

## Epic 3: Tata Kelola Kas (Multi-Signature 3-of-3)
*   Sebagai **Bendahara**, saya ingin **membuat draf proposal pengeluaran kas** sehingga **dana siap dikunci di *blockchain* dengan status *Pending*.**
*   Sebagai **Ketua / Wakil Ketua**, saya ingin **memberikan persetujuan (*approval*) secara digital dari *dashboard*** sehingga **syarat validasi pencairan dana terpenuhi.**
*   Sebagai **Sistem (Smart Contract)**, saya ingin **mengeksekusi transfer dana secara otomatis** sehingga **uang langsung cair ke tujuan sesaat setelah tiga tanda tangan terkumpul.**

## Epic 4: Otomasi Notifikasi (Backend Python)
*   Sebagai **Sistem (Backend)**, saya ingin **mendengarkan *event emission* dari jaringan *blockchain*** sehingga **saya mengetahui secara *real-time* jika ada transaksi pencairan yang sukses.**
*   Sebagai **Pengurus**, saya ingin **menerima laporan mutasi kas via pesan WhatsApp otomatis** sehingga **saya langsung mengetahui *update* keuangan tanpa harus membuka aplikasi terus-menerus.**