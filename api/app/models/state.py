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
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name
        }
        return hash
