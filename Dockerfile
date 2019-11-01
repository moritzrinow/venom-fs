FROM ubuntu:latest
LABEL maintainer="mrinow.dev@gmail.com"
RUN apt-get update -y && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y python3-venv

WORKDIR /app
RUN python3 -m venv venv
COPY ./requirements.txt .
RUN ./venv/bin/pip install -r requirements.txt
ENV FLASK_APP=venomfs
ENV FLASK_ENV=development
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV VENOM_FS_ROOT=/data
ENV VENOM_FS_SAFE=1
COPY ./venomfs ./venomfs
CMD ["./venv/bin/python3", "-m", "flask", "run", "--host", "0.0.0.0"]