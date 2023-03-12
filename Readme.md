# Using the JSON data type with MySQL 8 and Sqlalchemy

This project will show how JSON data type works in MySQL 8.
We will create a database using [percona-server:8.0](https://hub.docker.com/r/percona/percona-server/tags) and then we will create the tables using Python with **sqlalchemy** and finally insert some data in the database.

We are working with **Docker compose**. if you want to turn off the services use this command:

```bash
docker compose up
```

This command will start two services, one is the **db** which uses the image of [percona-server:8.0](https://hub.docker.com/r/percona/percona-server/tags) and the second service is called "api" which is a Python application with a Dockerfile. It wil create tables and insert some data in the database using **sqlalchemy**.

If you wanna see all the services:

```bash
docker compose ps
```

If you wanna turn down your services:

```bash
docker compose down
```

Checking the data in the database

```bash
docker exec db /bin/bash
```

```bash
show databases;
use library;
show tables;
select * from book;
describe book;
```

**Note** This projects is open source feel free to send feedbacks or suggestions
