import uvicorn

from app_python.config import config

if __name__ == "__main__":
    uvicorn.run("app_python.server:app",
                host=config.server_host,
                port=config.server_port,
                reload=True)
