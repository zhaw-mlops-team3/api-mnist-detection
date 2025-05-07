from functools import lru_cache
import wandb
import torch


@lru_cache
def get_model(artifact_name: str):
    run = wandb.init()

    artifact = run.use_artifact(artifact_name, type="model")
    artifact_dir = artifact.download()

    model = torch.load(artifact_dir + "/model.pth")

    return model


class DetectionService:
    def __init__(self, artifact_name: str):
        self._model = get_model(artifact_name)

    def detect(self, image):
        # Perform detection using the model
        results = self.model.detect(image)
        return results
