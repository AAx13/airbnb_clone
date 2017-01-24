from app import app
from app.models.user import User
from peewee import *
from flask_json import as_json, jsonify, request

@app.route('/users', methods=['GET', 'POST'])
@as_json
def get_users():

    if request.method == 'GET':
        user_query = User.select()
        users = [i.to_hash() for i in user_query] #<---
        return jsonify(users)

    elif request.method == 'POST':

        user = User.create(
            email=request.form['email'],
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            password=""
        )
        user.set_password(request.form['password'])
        return user.to_hash()
