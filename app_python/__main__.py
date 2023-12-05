import json
import os

import uvicorn

from app_python.config import config

if __name__ == "__main__":
    if not os.path.isfile(config.counter_file_path):
        with open(config.counter_file_path, 'w+') as f:
            f.write(json.dumps({'visits': 0}))
    uvicorn.run("app_python.server:app",
                host=config.server_host,
                port=config.server_port,
                reload=True)
