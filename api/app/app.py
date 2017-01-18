from app import app
from config import *

'''
This script will start the Flask application
'''

app.run(host=HOST, port=PORT, debug=DEBUG)
