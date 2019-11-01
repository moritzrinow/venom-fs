FROM python:latest
LABEL maintainer="mrinow.dev@gmail.com"
WORKDIR /app
RUN python -m venv venv
COPY ./requirements.txt .
RUN ./venv/scripts/pip install -r requirements.txt
ENV FLASK_APP=venomfs
ENV FLASK_ENV=development
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV VENOM_FS_ROOT="C:/data"
ENV VENOM_FS_SAFE=1
COPY ./venomfs ./venomfs
CMD ["./venv/scripts/python", "-m", "flask", "run", "--host", "0.0.0.0"]