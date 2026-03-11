import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from log_config import setup_logging
from db.connector import engine, Base, SessionLocal
from routers import test_router

setup_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Automatic create all tables during startup
    Base.metadata.create_all(bind=engine)

    yield

app = FastAPI(
    title="FastAPI App",
    lifespan=lifespan
)

# Middleware
origins = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Routers
app.include_router(
    test_router.router,
    prefix="/api/test",
    tags=["Test Router"]
)

@app.get("/")
async def root():
    return {"message": "App is running"}

@app.get("/test-db")
async def test_db():
    try:
        with SessionLocal() as db:
            result = db.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            
            logger.info("Successfully connected to the database.")
            return {
                "status": "success",
                "database_version": version
            }
            
    except Exception as e:
        logger.error(f"Error connecting to the database: {e}")
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
