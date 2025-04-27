from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, declarative_base

from app.configs.configs import Configs
from app.logs import get_logger
logger = get_logger(__name__)


engine = create_engine(Configs.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    Dependency that provides a database session for FastAPI routes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_db_n_tables():
    """
    Create the database and tables if they do not exist.
    """

    from app import models

    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()

    all_model_tables = Base.metadata.tables.keys()
    missing_tables = [t for t in all_model_tables if t not in existing_tables]

    if missing_tables:
        logger.info(f"Creating missing tables: {missing_tables}")
        Base.metadata.create_all(bind=engine)
    else:
        logger.info("All tables already exist. No action taken.")