import peewee
from peewee import *
from config import *
from datetime import datetime

''' Database variable utilizes MySQLDatabase method to draw database information along with configurations from config.py '''
db = MySQLDatabase(DATABASE['database'],
    host=DATABASE['host'],
    user=DATABASE['user'],
    port=DATABASE['port'],
    charset=DATABASE['charset'],
    passwd=DATABASE['password'])

''' BaseModel class inherits from peewee.Model. Among the declared public class attributes we have,
id: which returns a PrimaryKeyField object giving this field a unique id whenever a table is created.
created_at: returns the current date and time a table is created.
updated_at: returns the current date and time a table is updated.
'''
class BaseModel(peewee.Model):
    id = PrimaryKeyField(unique=True)
    created_at = DateTimeField(default=datetime.now, formats='%Y/%M/%d %H:%M:%S')
    updated_at = DateTimeField(default=datetime.now, formats='%Y/%M/%d %H:%M:%S')

    '''
    When this method is called, it will update current date and time to updated_at
    attribute before being called by its parent class.
    '''
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return method.save(self, *args, **kwargs)
        #return super(BaseModel, self).save(self, *args, **kwargs) not 100% sure what super() does yet

    class Meta():
        database = db
        order_by = ("id", )
