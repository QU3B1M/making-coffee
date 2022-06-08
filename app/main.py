from fastapi import FastAPI
# making-coffee imports
from db import init_database

app = FastAPI()

init_database(app=app)
