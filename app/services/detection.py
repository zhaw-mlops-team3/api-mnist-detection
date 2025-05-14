import wandb
import torch
import os
import base64
import torchvision.transforms as transforms

from functools import lru_cache
from io import BytesIO
from PIL import Image
from app.net import Net


@lru_cache
def get_model():
    wandb.login(key=os.getenv("WANDB_API_KEY"))
    run = wandb.init()

    artifact = run.use_artifact(
        artifact_or_name=os.getenv("WANDB_ARTIFACT_NAME"),
        type="model",
    )
    artifact_dir = artifact.download()
    model_path = next(
        (
            os.path.join(artifact_dir, file)
            for file in os.listdir(artifact_dir)
            if file.endswith(".pth")
        ),
        None,
    )
    if model_path is None:
        raise FileNotFoundError("No .pth file found in the artifact directory.")

    model = Net()
    model.load_state_dict(torch.load(model_path))
    model.eval()

    return model


class DetectionService:
    def __init__(self):
        self._model = get_model()

    def detect(self, imageBase64):
        image_data = base64.b64decode(imageBase64)
        image = Image.open(BytesIO(image_data)).convert("L")

        transform = transforms.Compose(
            [
                transforms.Resize((28, 28)),
                transforms.ToTensor(),
                transforms.Normalize((0.1307,), (0.3081,)),
            ]
        )
        image_tensor = transform(image).unsqueeze(0)

        with torch.no_grad():
            results = self._model(image_tensor)
            predicted_class = torch.argmax(results, dim=1).item()

        return predicted_class
