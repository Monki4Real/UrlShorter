import secrets
import string
from sqlalchemy.orm import Session
from app.models import UrlsBase 


def generate_short_code(db:Session, length: int = 8) -> str:
    alphabet = string.ascii_letters + string.digits
    
    while True:
        short_code = ''.join(secrets.choice(alphabet) for _ in range(length))

        existing = db.query(UrlsBase).filter(UrlsBase.short_code == short_code).first()

        if not existing:
            return short_code
