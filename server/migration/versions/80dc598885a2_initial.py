"""initial

Revision ID: 80dc598885a2
Revises: 
Create Date: 2024-09-15 04:13:40.352736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80dc598885a2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False, comment='Имя'),
    sa.Column('surname', sa.String(), nullable=False, comment='Фамилия'),
    sa.Column('patronymic', sa.String(), nullable=True, comment='Отчество'),
    sa.Column('bio', sa.String(), nullable=True, comment='Биография'),
    sa.PrimaryKeyConstraint('id'),
    comment='Авторы'
    )
    op.create_table('genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False, comment='Название жанра'),
    sa.Column('description', sa.String(), nullable=False, comment='Описание жанра'),
    sa.PrimaryKeyConstraint('id'),
    comment='Справочник книжных жанров'
    )
    op.create_table('publisher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False, comment='Название издательства'),
    sa.Column('description', sa.String(), nullable=False, comment='Описание издательства'),
    sa.PrimaryKeyConstraint('id'),
    comment='Справочник издательств'
    )
    op.create_table('book',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False, comment='Название книги'),
    sa.Column('description', sa.String(), nullable=False, comment='Описание книги'),
    sa.Column('isbn', sa.String(), nullable=False, comment='ISBN-идентификатор'),
    sa.Column('photo', sa.String(), nullable=True, comment='Ссылка на фотографию книги'),
    sa.Column('publisher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['publisher_id'], ['publisher.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isbn'),
    comment='Книги'
    )
    op.create_table('author_book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('author_id', 'book_id', name='uix_authority'),
    comment='Отношение авторства'
    )
    op.create_table('genre_book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.UUID(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('book_id', 'genre_id', name='uix_genres'),
    comment='Жанры у книг'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('genre_book')
    op.drop_table('author_book')
    op.drop_table('book')
    op.drop_table('publisher')
    op.drop_table('genre')
    op.drop_table('author')
    # ### end Alembic commands ###
