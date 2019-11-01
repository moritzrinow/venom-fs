# venom-fs
Simple RESTful file delivery to play around with.

## Install

#### Install python

#### Create virtual Python environment
python -m venv venv

#### Install modules
Linux:
./venv/bin/pip install -r requirements.txt

Windows:
venv\scripts\pip install -r requirements.txt

## Run

#### Define environment variables

set FLASK_APP=venomfs
set FLASK_ENV=development
set VENOM_FS_ROOT=data

Linux:
./venv/bin/python3 -m flask run

Windows:
venv\scripts\python -m flask run

### Docker

Linux:
docker build -t venomfs .
docker run -it -p 5000:5000 --name venomfs venomfs

Windows:
docker build -t venomfs -f Windows.Dockerfile .
docker run -it -p 5000:5000 --name venomfs venomfs
