from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String

from core.database.db import Base


class Encryption(Base):
    __tablename__ = 'encryption'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    encrypted_text = Column(String, index=True, nullable=False)
    decrypted_text = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return f'<Encryption {self.id}>'
