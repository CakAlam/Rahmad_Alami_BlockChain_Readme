from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import datetime

# Schema untuk Request (Input)
class ProposalCreate(BaseModel):
    judul_kegiatan: constr(min_length=5, max_length=100)
    nominal: float = Field(gt=0, description="Nominal harus lebih dari 0")

# Schema untuk Response (Output) - Sinkron dengan OpenAPI
class UserResponse(BaseModel):
    id: int
    nama: str
    role: str
    wallet_address: Optional[str] = None
    # Sangat Penting: Tidak ada field password di sini (Mencegah kebocoran data)

class ProposalResponse(BaseModel):
    id: int
    user_id: int
    judul_kegiatan: str
    nominal: float
    status: str
    tx_hash: Optional[str] = None
    created_at: datetime

class AIAnomalyResponse(BaseModel):
    is_anomaly: bool
    confidence_score: float
    reason: str
    fallback_used: bool = False