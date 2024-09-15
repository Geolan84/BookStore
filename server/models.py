from uuid import UUID

from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID

from database import Base


class Publisher(Base):
    __tablename__ = 'publisher'
    __table_args__ = {
        'comment': 'Справочник издательств'
    }
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False, comment="Название издательства")
    description: str = Column(String, nullable=False, comment="Описание издательства")
    books = relationship('Book', back_populates='publisher')


class Author(Base):
    __tablename__ = 'author'
    __table_args__ = {
        'comment': 'Авторы'
    }                                   
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False, comment="Имя")
    surname: str = Column(String, nullable=False, comment="Фамилия")
    patronymic: str = Column(String, comment="Отчество")
    bio: str = Column(String, comment="Биография")


class Book(Base):
    __tablename__ = 'book'
    __table_args__ = {
        'comment': 'Книги'
    }            
    id: UUID = Column(PostgresUUID, primary_key=True)
    name: str = Column(String, nullable=False, comment="Название книги")
    description: str = Column(String, nullable=False, comment="Описание книги")
    isbn: str = Column(String, nullable=False, unique=True, comment="ISBN-идентификатор")
    photo: str | None = Column('photo', String, comment="Ссылка на фотографию книги")
    publisher_id = Column(Integer, ForeignKey('publisher.id'), nullable=False)
    publisher = relationship('Publisher', back_populates="books")


class AuthorBook(Base):
    __tablename__ = 'author_book'
    __table_args__ = (
        UniqueConstraint('author_id', 'book_id', name='uix_authority'),
        {
            'comment': 'Отношение авторства'
        }
    )
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    book_id = Column(PostgresUUID, ForeignKey('book.id'))


class Genre(Base):
    __tablename__ = 'genre'
    __table_args__ = {
        'comment': 'Справочник книжных жанров'
    }                                   
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False, comment="Название жанра")
    description: str = Column(String, nullable=False, comment="Описание жанра")


class GenreBook(Base):
    __tablename__ = 'genre_book'
    __table_args__ = (
        UniqueConstraint('book_id', 'genre_id', name='uix_genres'),
        {
            'comment': 'Жанры у книг'
        }
    )
    id = Column(Integer, primary_key=True)
    book_id = Column(PostgresUUID, ForeignKey('book.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))
