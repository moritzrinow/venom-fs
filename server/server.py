from flask import Flask, request, Response, send_file
from flask import current_app as app
from flask import Blueprint
import server.fs as fs
import ntpath
import json

file_bp = Blueprint("_file", __name__, url_prefix='/_file')
dir_bp = Blueprint("_dir", __name__, url_prefix='/_dir')

file_service = fs.FileService()

@file_bp.route('/has', methods=['GET'])
def has_file():
  path = request.args.get('path')
  if not file_service.valid_path(path):
    return Response(status=400)

  return file_service.has_file(path)

@file_bp.route('/', methods=['GET'])
def get_file():
  path = request.args.get('path')
  if not file_service.valid_path(path):
    return Response(status=400)

  data = file_service.get_file(path)
  if data is None:
    return Response(status=400)

  fname = ntpath.basename(path)
  return send_file(data, attachment_filename=fname, mimetype='application/octet-stream')

@file_bp.route('/', methods=['POST'])
def put_file():
  path = request.args.get('path')
  if not file_service.valid_path(path):
    return Response(status=400)

  data = request.data

  file_service.put_file(path, data)
  return Response(status=201)

@file_bp.route('/list', methods=['GET'])
def list_file():
  path = request.args.get('path')
  if path is None:
    path = ''

  if not file_service.valid_path(path):
    return Response(status=400)

  files = file_service.list_file(path)
  if files is None:
    return Response(status=400)
  
  return Response(json.dumps(files), mimetype='application/json')

@dir_bp.route('/list', methods=['GET'])
def list_dir():
  path = request.args.get('path')
  if path is None:
    path = ''

  if not file_service.valid_path(path):
    return Response(status=400)

  directories = file_service.list_dir(path)
  if directories is None:
    return Response(status=400) 

  return Response(json.dumps(directories), mimetype='application/json')