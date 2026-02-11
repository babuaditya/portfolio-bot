FROM rasa/rasa-sdk:3.6.2

WORKDIR /app


# Install dependencies as root
USER root

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy action code
COPY . /app

EXPOSE 5055

CMD ["start", "--port", "5055", "--cors", "*", "--debug"]
