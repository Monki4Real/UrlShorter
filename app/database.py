from sqlalchemy import create_engine, sessionmaker
from models import Base
from config import settings

engine = create_engine(settings.DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(engine)

def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()



def create_db_and_tables() -> None:
    Base.metadata.create_all(engine)



