# Prompt Log: Software Requirements Specification (SRS)

**Dokumen ini berisi rekam jejak prompt yang digunakan untuk menyusun spesifikasi teknis perangkat lunak (SRS).**

---

**Prompt 1 (Translasi PRD ke SRS):**
> "Berdasarkan PRD sistem Hybrid App IPNU-IPPNU yang sudah dibuat, tolong buatkan dokumen Software Requirements Specification (SRS). Bagi menjadi Kebutuhan Fungsional, Kebutuhan Non-Fungsional, dan Arsitektur Sistem (Tech Stack)."

**Prompt 2 (Detailing Logika Smart Contract & Kriptografi):**
> "Pada bagian Kebutuhan Fungsional, tolong buat lebih spesifik. Masukkan logika matematis untuk Multi-Signature: P_exec = f(K_ketua) ∩ f(K_wakil) ∩ f(K_bendahara). Pada bagian Non-Fungsional, jelaskan juga bahwa sistem harus menggunakan algoritma kriptografi ECDSA bawaan Ethereum untuk validasi tanda tangan."

**Prompt 3 (Detailing Backend & Event Listener):**
> "Tambahkan spesifikasi teknis untuk fitur notifikasi WhatsApp. Jelaskan di Kebutuhan Fungsional bahwa backend (Python dengan library Web3.py) harus bertindak sebagai 'Event Listener' yang mendengarkan event emisi dari Smart Contract secara asinkronus, dengan batas toleransi delay maksimal 10 detik di Kebutuhan Non-Fungsional."