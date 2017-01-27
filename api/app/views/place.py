from app import app

@app.route()



'''
route /places:
GET: list of all places
POST: create a new place from POST data parameters (owner and city should be set by ID).
route /places/<place_id>:
GET: place with id = place_id
PUT: update the place with id = place_id with PUT data parameters. owner and city can't be changed
DELETE: delete place with id = place_id
route /states/<state_id>/cities/<city_id>/places:
GET: list of all places in the selected city
POST: create a new place from POST data parameters in the selected city.
'''
