FROM python:3.12.1-slim
WORKDIR /app
EXPOSE 8000
COPY requirements.txt ./

RUN pip install --no-cache --no-cache-dir -r requirements.txt

COPY ./src ./

CMD ["fastapi", "run", "/app/main.py"]
