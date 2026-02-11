FROM rasa/rasa:3.6.20

WORKDIR /app
COPY . /app

EXPOSE 5005

# IMPORTANT: clear base image ENTRYPOINT
ENTRYPOINT []

# Correct Rasa start command
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug"]
