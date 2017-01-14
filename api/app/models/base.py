import peewee
from peewee import *
from config import *
from datetime import *

database = MySQLDatabase(DATABASE['database'],
    host=DATABASE['host'],
    user=DATABASE['user'],
    port=DATABASE['port'],
    charset=DATABASE['charset'],
    passwd=DATABASE['password'])

class BaseModel(peewee.Model):
    id = PrimaryKeyField(unique=True)
    created_at = DateTimeField(default=datetime.now, formats='%Y/%M/%d %H:%M:%S')
    updated_at = DateTimeField(default=datetime.now, formats='%Y/%M/%d %H:%M:%S')

    def save(self, *args, **kwargs):
        self.update_at = datetime.now()

    class Meta():
        database = database
        order_by = ("id", )
