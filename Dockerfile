FROM rasa/rasa:3.6.20

WORKDIR /app
COPY . /app

USER root
RUN chmod +x /app/entrypoint.sh
USER 1001

ENTRYPOINT ["/app/entrypoint.sh"]
