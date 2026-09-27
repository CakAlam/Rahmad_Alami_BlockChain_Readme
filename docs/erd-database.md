erDiagram
    USERS {
        int id PK
        string nama
        string role "Enum: Anggota, Bendahara, Wakil, Ketua"
        string wallet_address "Nullable, untuk pengurus"
    }
    
    PROPOSALS {
        int id PK
        int user_id FK
        string judul_kegiatan
        decimal nominal
        string status "Enum: Draft, Pending, Approved, Executed"
        string tx_hash "Bisa null jika belum dieksekusi"
        datetime created_at
    }
    
    TRANSACTIONS {
        int id PK
        int proposal_id FK
        string tx_hash "Unik dari Blockchain"
        decimal gas_used
        datetime executed_at
    }

    USERS ||--o{ PROPOSALS : "mengajukan (Bendahara)"
    PROPOSALS ||--o| TRANSACTIONS : "menghasilkan"