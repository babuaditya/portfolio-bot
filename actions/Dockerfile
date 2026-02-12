FROM rasa/rasa-sdk:3.6.2

WORKDIR /app

USER root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER 1001

EXPOSE 5055
CMD ["start", "--port", "5055", "--cors", "*", "--debug"]
