import peewee
from peewee import *
from base import *

database.connect()
database.create_tables([Amenity, City, PlaceAmenities, PlaceBook, State, User])
