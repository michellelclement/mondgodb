import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'MS3_project'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')