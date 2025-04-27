from sqlalchemy import Column, Integer, String, func, DateTime

from app.database import Base


class URL(Base):
    """
    URL model for the database.
    """
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    clicks = Column(Integer, default=0) # The number of clicks on the shortened URL.