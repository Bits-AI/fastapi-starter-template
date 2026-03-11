from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class TestResponse(BaseModel):
    status: str = Field(..., example="OK")
    received_at: datetime = Field(..., example="2026-03-11T15:15:00")

    model_config = ConfigDict(from_attributes=True)
