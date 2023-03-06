FROM python:3

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.5 \
    python3-pip \
    nano \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install sqlalchemy PyMySQL cryptography


WORKDIR /app

COPY app/* /app


#CMD ["python3", "db.py"]

