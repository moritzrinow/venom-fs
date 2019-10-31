from flask import Flask, request
import os

def create_app():
  app = Flask(__name__)

  @app.route('/')
  def ping():
    return "PONG"

  from server.server import file_bp, dir_bp

  app.register_blueprint(file_bp)
  app.register_blueprint(dir_bp)

  return app