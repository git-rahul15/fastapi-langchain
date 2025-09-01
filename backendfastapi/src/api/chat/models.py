from sqlmodel import SQLModel, Field, DateTime
from datetime import datetime

class ChatMessageData(SQLModel):
    message: str


class ChatMessage(SQLModel, table=True):
    id: int | None = Field(default = None,primary_key=True)
    message: str
    created_at: datetime = Field(default_factory=datetime.utcnow, sa_type=DateTime(timezone=True),primary_key=False, nullable=False)

class ChatMessageItems(SQLModel):
    message:str
    created_at: datetime=Field(default=None)