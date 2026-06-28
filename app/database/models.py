from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False, unique=True)
    status = Column(String, nullable=False)

    files = relationship(
        "File",
        back_populates="repository",
        cascade="all, delete-orphan",
    )


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

    repository = relationship(
        "Repository",
        back_populates="files",
    )

    functions = relationship(
        "Function",
        back_populates="file",
        cascade="all, delete-orphan",
    )


class Function(Base):
    __tablename__ = "functions"

    id = Column(Integer, primary_key=True, index=True)

    file_id = Column(
        Integer,
        ForeignKey("files.id"),
        nullable=False,
    )

    name = Column(String, nullable=False)
    line = Column(Integer, nullable=False)

    file = relationship(
        "File",
        back_populates="functions",
    )
