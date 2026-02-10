
FROM rasa/rasa-sdk:3.6.2

WORKDIR /app

COPY ./ app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt
