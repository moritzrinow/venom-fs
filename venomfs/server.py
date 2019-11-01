from flask import Flask, request, Response, send_file
from flask import current_app as app
from flask import Blueprint
from .fs import FileService
import ntpath
import json
import io
import platform
import os

file_bp = Blueprint('_file', __name__, url_prefix='/_file')
dir_bp = Blueprint('_dir', __name__, url_prefix='/_dir')

system = platform.system()

safe = os.environ.get('VENOM_FS_SAFE')
if not safe is None:
  if safe == '0':
    safe = False
else:
  safe = True

file_service = FileService(safe_paths=safe)

def determine_root():
  if system == 'Windows':
    return 'C:\\ProgramData\\venomfs'

  if system == 'Linux':
    return 'data'

def init_server():
  root = os.environ.get('VENOM_FS_ROOT')
  if root is None:
    root = determine_root()

  print('Root specified: ', root)
  if not os.path.isdir(root):
    try:
      print('Root directory does not exit. Creating...')
      os.mkdir(root)
    except:
      print('Error while creating root directory. Invalid root directory: ', root)
      exit(1)
  
  print('Safe paths: ', safe)

  file_service.root = root

@file_bp.route('/has', methods=['GET'])
def has_file():
  path = request.args.get('path')
  if path is None:
    return Response('No path specified', status=400)
  
  if not file_service.is_safe_path(path):
    return Response('Invalid path: ' + path, status=400)
    
  try:
    exists = file_service.has_file(path)
  except:
    return Response('Something went wrong', status=500)

  if exists:
    return 'True'
  else:
    return 'False'

@file_bp.route('/', methods=['GET'])
def get_file():
  path = request.args.get('path')
  if not file_service.is_safe_path(path):
    return Response('Invalid path: ' + path, status=400)

  try:
    data = file_service.get_file(path)
  except:
    return Response('Something went wrong', status=500)

  if data is None:
    return Response('File not found', status=400)

  fname = os.path.basename(path)
  return send_file(io.BytesIO(data), attachment_filename=fname, mimetype='application/octet-stream')

@file_bp.route('/', methods=['POST'])
def put_file():
  path = request.args.get('path')
  if not file_service.is_safe_path(path):
    return Response('Invalid path: ' + path, status=400)

  data = request.data

  try:
    file_service.put_file(path, data)
  except:
    return Response('Invalid path', status=400)

  return Response(status=201)

@file_bp.route('/list', methods=['GET'])
def list_file():
  path = request.args.get('path')
  if path is None:
    path = ''

  if not file_service.is_safe_path(path):
    return Response('Invalid path: ' + path, status=400)

  try:
    files = file_service.list_file(path)
  except:
    return Response('Something went wrong', status=500)

  if files is None:
    return Response(status=400)
  
  return Response(json.dumps(files), mimetype='application/json')

@dir_bp.route('/list', methods=['GET'])
def list_dir():
  path = request.args.get('path')
  if path is None:
    path = ''

  if not file_service.is_safe_path(path):
    return Response('Invalid path: ' + path, status=400)

  try:
    directories = file_service.list_dir(path)
  except:
    return Response('Something went wrong', status=500)

  if directories is None:
    return Response(status=400) 

  return Response(json.dumps(directories), mimetype='application/json')