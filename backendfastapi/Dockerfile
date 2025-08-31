FROM python:3.13.4-slim-bullseye

RUN python -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY /src .


RUN uvicorn main:app --host 0.0.0.0 --port 8000