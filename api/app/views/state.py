from app import app
from app.models.state import State
from flask_json import jsonify, request


@app.route('/states', methods=['GET', 'POST'])
def states():

    if request.method == 'GET':

        state_query = State.select()
        res = [i.to_hash() for i in state_query]

        if res:
            return jsonify(res)
        else:
            output = {'error': 'No results found'}
            res = jsonify(output)
            res.status_code = 404
            return res

    elif request.method == 'POST':

        duplicate_name = State.select().where(State.name == request.form['name'])

        if not duplicate_name:

            state = State.create(
                name=request.form['name']
            )
            return jsonify(state.to_hash())


        output = {'code': 10001, 'msg': 'State already exists'}
        res = jsonify(output)
        res.status_code = 409
        return res

@app.route('/states/<state_id>', methods=['GET', 'DELETE'])
def states_id(state_id):

    if request.method == 'GET':

        state_query = State.get(State.id == state_id)
        return jsonify(state_query.to_hash())

    elif request.method == 'DELETE':

        state_query = State.get(State.id == state_id)
        state_query.delete_instance()
        state_query.save()
        response = {'msg': 'Deleted state at id: ' +  state_id }
        return jsonify(response)
