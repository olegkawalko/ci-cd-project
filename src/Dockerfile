FROM python:3.14.2-slim-bookworm

WORKDIR /app

COPY req.txt .

RUN pip install -r req.txt

COPY last_price.json .

COPY main.py . 

CMD ["python3", "main.py"]