FROM python:3.11
WORKDIR /code

ARG WANDB_ARTIFACT_NAME
ARG WANDB_API_KEY
ENV WANDB_ARTIFACT_NAME=${WANDB_ARTIFACT_NAME}
ENV WANDB_API_KEY=${WANDB_API_KEY}

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
CMD ["fastapi", "run", "app/main.py", "--port", "8080"]