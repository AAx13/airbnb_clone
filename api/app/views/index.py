from app import app
from app.models.base import *
from datetime import *
from flask_json import as_json, jsonify


@app.route('/', methods=['GET'])
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
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response

@app.errorhandler(404)
def not_found(error):
    data = {
        'code': 404,
        'msg': "not found"
    }
    error = jsonify(data)
    error.status_code = 404
    return error
