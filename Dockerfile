FROM python:3.11
WORKDIR /code

ARG MODEL
ENV MODEL=${MODEL}

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
CMD ["fastapi", "run", "app/main.py", "--port", "8080"]