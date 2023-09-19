from fastapi import APIRouter
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")

# Define a route for the root URL ("/") to serve index.html
@router.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("static/index.html")
