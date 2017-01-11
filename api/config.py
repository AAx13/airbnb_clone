import os

#===============================================================================#
# This script will set variables based on the current AIRBNB_ENV variable value #
#===============================================================================#

# Get value of current AIRBNB_ENV environment variable value

env_var = os.environ.get('AIRBNB_ENV')


# This if statement will assign variables when AIRBNB_ENV is set to development or production

if env_var == 'development':
    DEBUG = True
    HOST = 'localhost'
    PORT = 3333
    DATABASE = { 'host': '158.69.78.239',
                 'user': 'airbnb_user_dev',
                 'database': 'airbnb_dev',
                 'port': '3306',
                 'charset': 'utf8',
                 'password': os.environ.get('AIRBNB_DATABASE_PWD_DEV')}
    
elif env_var == 'production':
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 3000
    DATABASE = { 'host': '158.69.78.239',
                 'user': 'airbnb_user_prod',
                 'database': 'airbnb_prod',
                 'port': '3306',
                 'charset': 'utf8',
                 'password': os.environ.get('AIRBNB_DATABASE_PWD_PROD')}
                 
                 

