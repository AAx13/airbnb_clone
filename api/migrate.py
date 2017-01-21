import peewee
from peewee import *
from app.models import *

def create_tables():
    BaseModel.database.connect()
    BaseModel.database.create_tables([Amenity, City, PlaceAmenities, PlaceBook, State, User, Place])
