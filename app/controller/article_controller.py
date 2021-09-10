from flask import Flask, Blueprint, jsonify

article_api = Blueprint('article_api', __name__)

@article_api.route("/")
def index():
    return jsonify({"result":"ok"})

@article_api.route("/make")
def module_make():
    return jsonify({"result":"make"})