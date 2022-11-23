from flask import Flask
from flask_restx import Api


def create_app(env=None):
  from pokemon import register_routes
  app = Flask(__name__)
  api = Api(app, title="Flaskerific Pokemon API", version="0.0.1")

  register_routes(api)
  return app
