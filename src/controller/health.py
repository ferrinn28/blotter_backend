import logging

from fastapi import APIRouter

Health = APIRouter()

@Health.get("/health")
def hello_world():
    logging.info("Health Check")
    return {
        "status": "OK",
        "msg": "Application is ready"
        }