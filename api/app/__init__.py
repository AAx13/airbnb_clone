from flask import Flask

app = Flask(__name__)
json = FlaskJSON(app)

from views import *
