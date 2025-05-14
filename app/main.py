from fastapi import Depends, FastAPI
from app.models.detect import DetectModel
from app.services.detection import DetectionService

app = FastAPI()


@app.post("/detect")
async def detect(
    request_body: DetectModel, detection_service=Depends(DetectionService)
):
    detection = detection_service.detect(request_body.image)
    return detection
