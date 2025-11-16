from fastapi import FastAPI
import src.controller as routes

app = FastAPI()

app.include_router(routes.Health)
