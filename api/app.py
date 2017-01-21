from app import app
from config import *

'''
This script will start the Flask application
'''

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
