FROM python:3.10-slim

WORKDIR /app

COPY . .

ENV DATABASE_URL="postgresql://postgres:KBeAQc54WbhCtgPUhyNf@localhost:5432/todo"

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

EXPOSE 5000
ENTRYPOINT ["/app/entrypoint.sh"]