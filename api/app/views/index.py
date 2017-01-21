from app import app
from flask import Request, Response
from datetime import *
from flask_json import as_json
from app.models.base import BaseModel

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
    BaseModel.database.connect()

@app.after_request
def after_request(response):
    BaseModel.database.close()
    return response

@app.errorhandler(404)
@as_json
def not_found():
    data = {
        'code': 404,
        'msg': "not found"
    }
    return data
