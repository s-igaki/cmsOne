from flask import Flask
import yaml
from app.controller.article_controller import article_api
import os
import sys



if __name__ == "__main__":
      # アプリケーション起動
      app = Flask(__name__)

      # config設定
      args = sys.argv
      if (len(args) == 1):
            app.logger.error('please set env artument')
            exit(255)

      with open('config/config.yml', 'r') as yml:
        config = yaml.load(yml)[args[1]]
      app.config.update(
        config
      )

      # controller設定
      app.register_blueprint(article_api)
      app.run(host=app.config["host"], port=app.config["port"], debug=app.config["debug"])

