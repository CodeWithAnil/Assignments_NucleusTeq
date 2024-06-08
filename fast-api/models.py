from sqlalchemy import Column,Integer,VARCHAR
from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key = True, index = True)
    name = Column(VARCHAR(50))
    email = Column(VARCHAR(50))
