from fastapi import FastAPI
import os

app = FastAPI()
model = os.getenv("MODEL")


@app.get("/")
async def root():
    return {"message": model}
