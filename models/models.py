from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String(50), nullable=False)

    links = relationship("Link", back_populates="user")


class Link(Base):
    __tablename__ = 'link'

    id = Column(Integer, primary_key=True)
    original_url = Column(String, unique=True, nullable=False)
    short_url = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    get_counter = Column(Integer, default=0, nullable=False)

    user = relationship("User", back_populates="links")