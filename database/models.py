from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import DB_HOST, DB_USER, DB_PASSWORD, DB_PORT, DATABASE


connection_string = "postgresql+asyncpg://%s:%s@%s:%s/%s?async_fallback=True" % (DB_USER, DB_PASSWORD, DB_HOST, str(DB_PORT), DATABASE)

engine = create_async_engine(url=connection_string)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True)
    tasks: Mapped[str] = mapped_column(String())


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
