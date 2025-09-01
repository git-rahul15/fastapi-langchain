from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session, select
from .models import ChatMessageData, ChatMessage, ChatMessageItems
from api.db import get_session

router = APIRouter()

@router.get("/healthz")
def chat_healthz():
    return {"status":"ok"}

@router.get("/recent", response_model=List[ChatMessageItems])
def chat_list_messages(session: Session=Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10]
    return results

@router.post("/", response_model =ChatMessage)
def chat_create_message(data:ChatMessageData,session: Session = Depends(get_session)):
    
    data = data.model_dump()

    print(data)
    object = ChatMessage.model_validate(data)
    session.add(object)
    session.commit()
    session.refresh(object)

    return object