FROM python:3.12.7-slim

WORKDIR /fastapiproject

COPY requirements.txt /fastapiproject/
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /fastapiproject/src
COPY .env/ /fastapiproject/

CMD ["python", "/fastapiproject/src/main.py"]
