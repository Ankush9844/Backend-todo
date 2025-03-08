FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

EXPOSE 5000
ENTRYPOINT ["/app/entrypoint.sh"]