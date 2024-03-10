from pathlib import Path
import uvicorn
from fastapi import FastAPI, Request, WebSocket
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import time
import os

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "custom_quiz_website" / "app" / "src" / "static"),
    name="static",
)

BASE_DIR = Path(__file__).resolve().parent / "app" / "src"

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

@app.get("/")
async def return_home_page(request: Request):
    return templates.TemplateResponse(
        "home.html",
        context={
            "request": request,
            "zip": zip
        }
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)