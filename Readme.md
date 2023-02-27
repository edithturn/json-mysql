# Using the JSON data type with MySQL 8

## Installing Percona Server MySQL (Docker)

```bash
docker run -d --name percona-server-1 -e MYSQL_ROOT_PASSWORD=root percona/percona-server:8.0
```

## Running Python with Sqlalchemy

We will now create a database and create the tables using Python with Sqlalchemy.

- First we will create the connection to Percona Server for MySQL
- We can run the program to create the databae, tables and insert the data
- We will list the data to see all the columns
- Let's focus in JSON datatype in Percona Server for MySQL

# Installing SQLAlchemy

```bash
pip install sqlalchemy PyMySQL
```

# Creating a virtual Python environment

```python
pip install virtualenv

python3 -m venv myenv
source myenv/bin/activate
```

# Check what Python Libraries are installed

```python
pip list
```

# Desactivate environment

```python
deactivate
```
