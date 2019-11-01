FROM ubuntu:latest
RUN apt-get update -y && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y python3-venv

WORKDIR /app
COPY ./requirements.txt .
COPY ./server ./server
RUN python3 -m venv venv
RUN ./venv/bin/pip install -r requirements.txt
ENV FLASK_APP=server
ENV FLASK_ENV=development
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
CMD ["./venv/bin/python3", "-m", "flask", "run", "--host", "0.0.0.0"]