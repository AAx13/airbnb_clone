import json
from flask import Request
from flask import Response
from datetime import *
from app import app
from flask_json import *
from app.models.base import *

@app.route('/', methods=["GET"])
@as_json
def index():
    utc = datetime.utcnow()
    local = datetime.now()

    data = {
        'status': 'OK',
        'utc_time': utc.strftime('%Y/%m/%d %H:%M:%S'),
        'time': local.strftime('%Y/%m/%d %H:%M:%S')
    }
    return data

@app.before_request
def before_request():
    database.connect()

@app.after_request
def after_request(response):
    database.close()
    return response

@app.errorhandler(404)
@as_json
def not_found():
    data = {
        'code': 404,
        'msg': "not found"
    }
    return data
