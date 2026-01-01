from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="LitePay API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "LitePay backend running"}

from app.db.session import engine
from app.db.base import Base

@app.on_event("startup")
def test_db():
    Base.metadata.create_all(bind=engine)
    print("Database tables created or verified.")