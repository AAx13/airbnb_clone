import peewee
from peewee import *
from app.models import *
from app.models.base import *

db.connect()
db.create_tables([Amenity, City, PlaceAmenities, PlaceBook, State, User, Place])
