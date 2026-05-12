from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


class UrlsBase(Base): 
    __tablename__ = "urls"

    id: Mapped[int]  = mapped_column(primary_key=True)
    short_code: Mapped[str] = mapped_column(unique=True, index=True)
    original_url: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    clicks: Mapped[int] = mapped_column(default=0)
    last_accessed: Mapped[datetime] = mapped_column(nullable=True, default=None)