"""
This file defines the routes for the root URL ("/") and the static files
"""
from fastapi import APIRouter
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/", response_class=HTMLResponse)
async def root():
    """ Define a route for the root URL ("/") to serve index.html """
    return FileResponse("static/index.html")
