FROM python:latest
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./server ./server
ENV FLASK_APP=server
ENV FLASK_ENV=development
CMD ["flask", "run", "--host", "0.0.0.0"]