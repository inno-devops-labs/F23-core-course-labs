from fastapi import FastAPI
from .routes import get_msk_time, index
from .settings import get_settings
import uvicorn
from fastapi.staticfiles import StaticFiles

app = FastAPI()
settings = get_settings()

app.include_router(get_msk_time.router)
app.include_router(index.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.app_port, reload=True)
