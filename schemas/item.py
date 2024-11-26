from datetime import datetime
from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=1000)

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = Field(None, max_length=1000)

class Item(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True 