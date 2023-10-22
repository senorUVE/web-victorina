FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./ /app
WORKDIR /app

RUN pip install fastapi[all] sqlalchemy databases requests

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
