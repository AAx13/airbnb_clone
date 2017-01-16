from peewee import *
import hashlib
from hashlib import *
from base import *

'''
Here I defined all attributes for user class and defined 'set_password' module
to convert a password into an md5 encoded string
'''

class User(BaseModel):
    email = CharField(max_length=128, unique=True, null=False)
    password = CharField(max_length=128, null=False)
    first_name = CharField(max_length=128, null=False)
    last_name = CharField(max_length=128, null=False)
    is_admin = BooleanField(default=False)
    
    def set_password(self, clear_password):
        md5pw = hashlib.md5()
        md5pw.update(clear_password)
        self.password = md5pw.hexdigest()
