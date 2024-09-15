from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData

from config import DATABASE_URL


Base = declarative_base()
engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)
metadata = MetaData()


async def sql_session():
    async with async_session() as _session:
        yield _session
