from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI

from app.database import create_db_n_tables, get_db
from app.logs import get_logger
from app.routers import url

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up...")
    # create necessary tables
    logger.info("Connecting to database...")
    try:
        from app.database import get_db
        conn = get_db()
        conn.send(None)  # Trigger the generator to establish a connection
        conn.close()  # Close the connection
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise
    logger.info("Database connection successful.")
    # create database and tables
    logger.info("Creating database and tables...")
    create_db_n_tables()
    logger.info("Database and tables created.")
    # Perform any startup tasks here
    logger.info("Application's ready...")
    yield
    print("Shutting down...")


app = FastAPI(title="URL Shortner API", version="1.0.0", lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Welcome to URL Shortner API"}
@app.get("/health")
async def health():
    return {"status": "healthy"}
@app.get("/status")
async def status():
    return {"status": "running"}
@app.get("/info")
async def info():
    return {"info": "This is a URL Shortner API. It shortens long URLs into shorter ones."}

app.include_router(
    url.router,
    tags=["URL"],
    # dependencies=[Depends(get_db)],  # Uncomment if you want to use the dependency for all routes, since we're checking the DB connection on startup, no need to add here
    # include_in_schema=False,  # Uncomment if you want to exclude this router from the OpenAPI schema
    # default_response_class=JSONResponse,  # Uncomment if you want to set a default response class
)