# syntax=docker/dockerfile:1

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

CMD ["python3", "-m" , "uvicorn", "main:app", "--reload", "--host=0.0.0.0"]
