from time import sleep

from fastapi import FastAPI, Depends
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn

from models import Book
from database import sql_session


app = FastAPI(title="BookStore API")


@app.get("/")
def read_root():
    return "Hello from BookStore."


@app.get("/books")
async def get_all_books(session: AsyncSession = Depends(sql_session)):
    result = await session.execute(sa.select(Book))
    sleep(4)
    return {
        'books': result.scalars().all()
    }


@app.get("/books/{bookId}")
async def get_book_by_id(bookId: str, session: AsyncSession = Depends(sql_session)):
    result = await session.execute(sa.select(Book).filter_by(id=bookId))
    return result.scalar_one_or_none()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", reload=True)
