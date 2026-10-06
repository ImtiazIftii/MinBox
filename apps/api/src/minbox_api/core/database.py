from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import(
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from minbox_api.core.config import settings

#Creating asynchronous database engine with connection pooling
#Echo = true prints the sql query in the terminal

engine = create_async_engine(
    settings.DATABASE_URL,
    echo = settings.ENVIRONMENT == "development",
    future = True,
)

#creates the session factory
#expire_on_commit = false prevents sql from needing extra queries
#to re-read object attributes after you commit them

async_session_maker = async_sessionmaker(
    bind = engine,
    class_ = AsyncSession,
    expire_on_commit = False,
    autocommit = False,
    autoflush = False,
)

#this is the base class for all future sqlalchemy models(User, PinedApp etc)

class Base(DeclarativeBase):
    pass


#FastAPI dependency: yields a database session per http request

async def get_db() -> AsyncGenerator[AsyncSession,None]:
    #ensures the session is closed when the request finishes

    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()
                