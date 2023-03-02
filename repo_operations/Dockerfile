# FROM python:3.8-slim-buster

# WORKDIR /app

# COPY requirements.txt requirements.txt

# RUN pip install -r requirements.txt

# COPY . .

# CMD [ "python3", "main.py" ]

FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["main.py" ]
