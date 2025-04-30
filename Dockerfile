
FROM python:3.9
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

ENV PORT 80
RUN pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "run", "app/main.py", "--port", "80"]