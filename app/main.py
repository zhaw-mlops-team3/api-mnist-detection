from fastapi import Depends, FastAPI
import os

from app.models.detect import DetectModel
from app.services.detection import DetectionService

app = FastAPI()
WANDB_ARTIFACT_NAME = os.getenv("WANDB_ARTIFACT_NAME")


@app.post("/detect")
async def detect(
    request_body: DetectModel, detection_service=Depends(DetectionService)
):
    return {"detection": 3}
