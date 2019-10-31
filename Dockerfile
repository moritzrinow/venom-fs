FROM ubuntu:latest
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
WORKDIR /app
COPY ./requirements.txt .
RUN pip install flask
COPY ./server ./server
ENV FLASK_APP=server
ENV FLASK_ENV=development
#CMD ["python", "-m","flask", "run", "--host", "0.0.0.0"]