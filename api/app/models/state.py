import peewee
from peewee import *
from base import *

'''
Added state class to inherit from basemodel which will only a name attribute
'''
class State(BaseModel):
    name = CharField(max_length=128, unique=True, null=False)

    def to_hash(self):
        hash = {
            'id': self.id,
            'created_at': self.created_at.strftime("%Y/%m/%d %H:%M:%S"),
            'updated_at': self.updated_at.strftime("%Y/%m/%d %H:%M:%S"),
            'name': self.name
        }
        return hash
