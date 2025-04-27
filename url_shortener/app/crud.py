from sqlalchemy.orm import Session
from app import models, schemas
import string, random


def generate_short_code(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def create_short_url(db: Session, url: schemas.URLCreate) -> models.URL:
    short_code = generate_short_code()
    
    # Ensure uniqueness (optional: can loop or handle conflict later)
    db_url = models.URL(original_url=str(url.original_url), short_url=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def get_url_by_short_code(db: Session, short_code: str):
    return db.query(models.URL).filter(models.URL.short_url == short_code).first()
