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

RUN chmod a+x run.sh

#COPY ./requirements.txt .
#RUN pip install -r requirements.txt
CMD bash -C './run.sh';'bash'


# To have Requirements.txt with dependencies
# pip3 install -r requirements.txt

