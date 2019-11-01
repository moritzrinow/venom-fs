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

FLASK_APP=venomfs  
FLASK_ENV=development  
VENOM_FS_ROOT=data  

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

## Usage

### Retreive file

GET /_file/?path=sample_dir/sample.json  
-> Binary file content  

### Check if file exists

GET /_file/has?path=sample_dir/sample.json  
-> "True" / "False"  

### Upload file

POST /_file/?path=sample_dir/sample.json [BODY]: Binary file content  
-> 201 if successful  

### List files of a directory

GET /_file/list?path=sample_dir  
-> []  

### List subdirectories of a directory

GET /_dir/list?path=sample_dir  
-> []  
