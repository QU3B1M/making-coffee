# Third-party imports
from fastapi import FastAPI
# making-coffee imports
from db import init_database
from api import router

app = FastAPI()

init_database(app=app)
app.include_router(router)
