from peewee import *
import config

database = peewee.MySQLDatabase(config.DATABASE['database'],
host=config.DATABASE['host'],
user=config.DATABASE['user'],
port=config.DATABASE['port'],
charset=config.DATABASE['charset'],
password=config.DATABASE['password'])

class BaseModel(peewee.Model):
    id = PrimaryKey(Unique)
