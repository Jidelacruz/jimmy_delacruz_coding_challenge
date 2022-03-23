# start by pulling the python image
# syntax=docker/dockerfile:1
FROM python:3.8

# switch working directory
WORKDIR /flask_docker

# copy the requirements file into the image
COPY requirements.txt requirements.txt

# install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY . .

ENV FLASK_APP=main.py

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0","--port=8888"]