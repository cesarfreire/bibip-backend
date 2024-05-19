FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    sqlite3 \
    python3-full \
    python3-pip

COPY . /app
WORKDIR /app

RUN python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

EXPOSE 8888

CMD [".venv/bin/uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8888", "--reload"]