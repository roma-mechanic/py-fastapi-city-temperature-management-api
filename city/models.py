from sqlalchemy import Column, Integer, String

from database import Base


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(125), unique=True, nullable=False)
    additional_info = Column(String(512), nullable=True)
