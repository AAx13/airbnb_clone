from app import app
from app.models.city import *
from app.models.state import *
from flask_json import jsonify, request

@app.route('/states/<state_id>/cities', methods=['GET', 'POST'])
def cities(state_id):

    if request.method == 'GET':

        city_query = City.select().join(State).where(State.id == state_id)
        res = [i.to_hash() for i in city_query]

        if res:
            return jsonify(res)
        else:
            output = {'error': 'No results found'}
            res = jsonify(output)
            res.status_code = 404
            return res

    elif request.method == 'POST':

        dup_name_id = City.select().where(City.name == request.form['name']).join(State).where(State.id == state_id)

        if not dup_name_id:
            city = City.create(
                name=request.form['name'],
                state_id=state_id
            )
            return jsonify(city.to_hash())

        else:
            output = {'code': 10002, 'msg': 'City already exists in this state'}
            res = jsonify(output)
            res.status_code = 409
            return res


@app.route('/states/<state_id>/cities/<city_id>', methods=['GET', 'DELETE'])
def del_cities(state_id, city_id):

    if request.method == 'GET':

        city_query = City.get(City.id == city_id)
        return jsonify(city_query.to_hash())

    elif request.method == 'DELETE':

        city_query = City.get(City.id == city_id)
        city_query.delete_instance()
        city_query.save()
        response = {'msg': 'Deleted city at id: ' +  city_id}
        return jsonify(response)
