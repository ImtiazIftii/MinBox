from sqlite3 import DateFromTicks
from datetime import datetime,timezone

from sqlalchemy import Boolean,DateTime,Integer,String,func

from sqlalchemy.orm import Mapped, mapped_column

from minbox_api.core.database import Base


#this represents a registered minbox user
class User(Base):
    __tablename__ = "users"

    #we do indexing to search values faster(usually for frequenly used values)
    id: Mapped[int] = mapped_column(Integer,primary_key = True, index = True) 

    email: Mapped[str] = mapped_column(
        String(255),
        unique = True,
        index = True,
        nullable = False,
    )

    #hashin the passsword

    hashed_passwrod: Mapped[str] = mapped_column(String(255), nullable = False)

    #Account status active or disabled
    is_active: Mapped[bool] = mapped_column(Boolean, default = True, nullable=False)

    #Auditing the timestamps(When created and deleted)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default = lambda: datetime.now(timezone.utc),
        server_default = func.now(),
        nullable = False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default = lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable = False,
    )


    def __repr__(self) -> str:
        return f"<User id={self.id} email = {self.email}>"