FROM python:3.9.23-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["app.py"]