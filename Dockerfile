FROM python:3

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.5 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install sqlalchemy PyMySQL

COPY app .

WORKDIR /app

CMD ["python", "db.py"]

