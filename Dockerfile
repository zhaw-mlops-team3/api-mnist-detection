FROM python:3.9
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
