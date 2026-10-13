from fastapi import Depends, FastAPI, status, HTTPException, Request, Response, Cookie
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from pathlib import Path

app = FastAPI(  
    title="TokenEconomyForKids API",
    description="Simple API for the TokenEconomyForKids project.",
    version="0.0.1",
)

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app.mount("/static", StaticFiles(directory=FRONTEND_DIR / "static"), name="static")

@app.get("/")
def read_root():
    return {"Hello": "World"}

