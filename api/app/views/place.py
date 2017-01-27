from app import app

@app.route('/places', methods=['GET', 'POST'])
def places():

    if request.method == 'GET':

        place_query = Place.select()
        res = [i.to_hash() for i in place_query]

        if res:
            return jsonify(res)
        else:
            error = {'error': 'No results found'}
            res = jsonify(output)
            res.status_code = 404
            return res

    elif request.method == 'POST':

        



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
