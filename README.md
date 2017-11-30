# docker-flask
An example of deploying a flask app with docker compose.

# Requirements
+ Docker
+ Docker Compose

# Installation
Download or clone the repo in your target directory. 

Then move to the folder containing the docker-compose.yml file.

First we will run
```python
docker-compose build
```
to build our web service. This web service is built with a Dockerfile inside docker-flask directory .

After that we will do
```python
docker-compose up -d
```
 to start our services in detached mode.

Finally
```python
docker-compose run web /usr/local/bin/python create_database.py
```
to create our table in the database.

# Usage
Now you can navigate to [localhost:8080](http://localhost:8080), [127.0.0.1:8080](http://127.0.0.1:8080) or [0.0.0.0:8080](http://0.0.0.0:8080).