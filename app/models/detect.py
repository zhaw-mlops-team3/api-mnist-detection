from pydantic import BaseModel


class DetectModel(BaseModel):
    image: str
