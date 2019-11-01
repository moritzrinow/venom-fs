from flask import Flask, request
import os

def create_app():
  app = Flask(__name__)

  @app.route('/')
  def ping():
    return "PONG"

  from .server import init_server, file_bp, dir_bp
  init_server()

  app.register_blueprint(file_bp)
  app.register_blueprint(dir_bp)

  return app