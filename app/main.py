from fastapi import FastAPI
import os

from app.models.detect import DetectModel

app = FastAPI()
model = os.getenv("MODEL")


@app.post("/detect")
async def detect(request_body: DetectModel):
    return {"detection": 3}
