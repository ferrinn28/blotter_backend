import logging

from fastapi import APIRouter

HealthController = APIRouter()

@HealthController.get("/health")
def health():
    logging.info("Health Check")
    return {
        "status": "OK",
        "msg": "Application is ready"
        }