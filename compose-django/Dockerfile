FROM python:3
# Setting PYTHONUNBUFFERED to a non empty value ensures that the python output is sent straight to terminal (e.g. your container log) without being first 
# buffered and that you can see the output of your application (e.g. django logs) in real time.
# This also ensures that no partial output is held in a buffer somewhere and never written in case the python application crashes.
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/