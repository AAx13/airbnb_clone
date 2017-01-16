from base import *

'''
Added state class to inherit from basemodel which will only a name attribute
'''
class State(BaseModel):
    name = CharField(max_length=128, unique=True, null=False)
