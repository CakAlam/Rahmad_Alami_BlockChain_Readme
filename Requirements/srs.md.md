# Software Requirements Specification (SRS)

## 1. Kebutuhan Fungsional (Functional Requirements)
* **FR-01 (Public Access):** Sistem harus memungkinkan Aktor Anggota untuk melihat tabel laporan kas dan mengeklik detail *hash* transaksi tanpa melalui proses autentikasi.
* **FR-02 (Web2 Auth):** Sistem harus memvalidasi *username* dan *password* pengurus di *database* lokal/Web2 sebelum memberikan akses ke *dashboard* internal.
* **FR-03 (Web3 Auth):** Sistem harus meminta *prompt* koneksi MetaMask (`eth_requestAccounts`) saat pengurus akan mengajukan atau menyetujui draf proposal keuangan.
* **FR-04 (Smart Contract Logic):** Sistem (Smart Contract) harus mengunci status proposal menjadi *Pending* hingga $P_{exec} = f(K_{ketua}) \cap f(K_{wakil}) \cap f(K_{bendahara})$ terpenuhi.
* **FR-05 (Event Listener):** *Backend* harus secara aktif mendengarkan (listen) *event* `TransactionExecuted` dari *smart contract* untuk memicu pengiriman pesan WhatsApp (UC-09).

## 2. Kebutuhan Non-Fungsional (Non-Functional Requirements)
* **NFR-01 (Integritas Data):** Setiap mutasi saldo kas harus diproses secara *on-chain* di jaringan *blockchain* (Testnet) sehingga datanya *immutable* (tidak dapat diubah/dihapus).
* **NFR-02 (Keamanan Autentikasi):** Sistem wajib menggunakan algoritma kriptografi ECDSA bawaan jaringan Ethereum untuk memvalidasi tanda tangan digital setiap pengurus.
* **NFR-03 (Performa Asinkronus):** Keterlambatan (*delay*) pengiriman notifikasi WhatsApp setelah *block* terkonfirmasi di jaringan maksimal adalah 10 detik.

## 3. Arsitektur Sistem & Tech Stack
* **Lapisan Web2 (Presentasi & Konten):** HTML, CSS, JavaScript (Frontend) dan *Database Server* ringan.
* **Lapisan Web3 (Interaksi Finansial):** Solidity Smart Contract (di-*deploy* di jaringan Sepolia Testnet).
* **Lapisan Integrasi & Backend:** Python, menggunakan *library* `Web3.py` untuk interaksi *blockchain* dan *library* pendukung API WhatsApp.