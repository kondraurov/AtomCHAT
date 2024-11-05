from pydantic import BaseModel, Field
from datetime import datetime


class MessageRead(BaseModel):
    id: int = Field(..., description="Уникальный идентификатор сообщения")
    sender_id: int = Field(..., description="ID отправителя сообщения")
    recipient_id: int = Field(..., description="ID получателя сообщения")
    content: str = Field(..., description="Содержимое сообщения")


class MessageCreate(BaseModel):
    recipient_id: int = Field(..., description="ID получателя сообщения")
    content: str = Field(..., description="Содержимое сообщения")

class MessageSchema(BaseModel):
    id: int
    sender_id: int
    recipient_id: int
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True