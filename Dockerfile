FROM python:3.11-alpine
RUN apk update && \
    apk add --no-cache libpq-dev && \
    apk add --no-cache gcc musl-dev
RUN pip install --no-cache-dir psycopg2
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
