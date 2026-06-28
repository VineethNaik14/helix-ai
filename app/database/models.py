from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False, unique=True)
    status = Column(String, nullable=False)

    files = relationship("File", back_populates="repository")


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    repository_id = Column(
        Integer,
        ForeignKey("repositories.id"),
        nullable=False,
    )

    path = Column(String, nullable=False)
    language = Column(String, nullable=False)

    repository = relationship("Repository", back_populates="files")
