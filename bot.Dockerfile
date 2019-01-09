from python:3.6-slim

run apt update && apt install -y git gcc make curl g++

run python -m pip install --upgrade pip

add bot/requirements.txt /tmp

run pip install --no-cache-dir -r /tmp/requirements.txt

run python -m spacy download pt

add ./bot /bot

workdir /bot

EXPOSE 5005
EXPOSE 5002

cmd make train-core - && make run-core