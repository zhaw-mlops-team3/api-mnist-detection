from fastapi import Depends, FastAPI
from app.models.detect import DetectModel
from app.services.detection import DetectionService

import os

app = FastAPI()
WANDB_ARTIFACT_NAME = os.getenv("WANDB_ARTIFACT_NAME")


@app.post("/detect")
async def detect(
    request_body: DetectModel, detection_service=Depends(DetectionService)
):
    detection = detection_service.detect(request_body.image)
    return detection


@app.get("/")
async def root():
    return {"message": WANDB_ARTIFACT_NAME}
