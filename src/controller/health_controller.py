import logging

from fastapi import APIRouter
from src.dto import HealthCheckResponse


HealthController = APIRouter(tags=["Health Check"])

@HealthController.get("/health")
def health() -> HealthCheckResponse:
    LOG_NAME = "HealthController" 
    logger = logging.getLogger(LOG_NAME)
    
    logger.info("Health Check")

    return HealthCheckResponse(
        status= "OK",
        msg= "Application is ready"
    )