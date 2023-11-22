import logging
import zoneinfo
from datetime import datetime

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

visitsNumberFilePath = "src/resources/visits"
app = FastAPI()
Instrumentator().instrument(app).expose(app)


@app.get("/")
async def root():
	increment_visits_number(visitsNumberFilePath)
	zone = zoneinfo.ZoneInfo("Europe/Moscow")
	return {"time": datetime.now(zone)}


@app.get("/visits")
async def get_visits():
	return read_visits_number(visitsNumberFilePath)


def increment_visits_number(filePath):
	try:
		with open(filePath, "r+") as f:
			current_number = int(f.read())
			f.seek(0)
			f.write(str(current_number + 1))
			f.truncate()
	except FileNotFoundError:
		logging.info(f"File in {filePath} not found. File will be created")
		create_file(filePath)


def read_visits_number(filePath) -> int:
	try:
		with open(filePath, "r") as f:
			return int(f.read())
	except FileNotFoundError:
		logging.info(f"File in {filePath} not found. File will be created")
		create_file(filePath)
		return 0


def create_file(filePath):
	with open(filePath, 'w+') as f:
		f.write("0")
