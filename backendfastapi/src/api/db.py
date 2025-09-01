from decouple import  config
import os
import sqlmodel
from sqlmodel import Session, SQLModel

DATABASE_URL = config('DATABASE_URL', default=None)

if DATABASE_URL == None:
    raise NotImplementedError("DATABASE_URL needs to be implemented")



engine = sqlmodel.create_engine(DATABASE_URL)

def db_init():
    print("creating db tables...")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session