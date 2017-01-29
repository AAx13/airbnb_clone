from app import app
from app.models.place_book import PlaceBook
from app.models.place import Place
from flask_json import jsonify, request


@app.route('/places/<place_id>/books', methods=['GET'])
def get_books(place_id):

    books_query = PlaceBook.select().join(Place).where(Place.id == place_id)
    res = [i.to_hash() for i in books_query]

    if res:
        return jsonify(res)

    output = {'error': 'No results found'}
    res = jsonify(output)
    res.status_code = 404
    return res


@app.route('/places/<place_id>/books', methods=['POST'])
def post_book(place_id):

    new_book = PlaceBook.create(
        place_id=place_id,
        user_id=request.form['user_id'],
        is_validated=request.form['is_validated'],
        date_start=request.form['date_start'],
        number_nights=request.form['number_nights']
    )
    return jsonify(new_book.to_hash())


@app.route('/places/<place_id>/books/<book_id>', methods=['GET'])
def get_book_by_id(place_id, book_id):

    book_query = PlaceBook.select().join(Place).where(Place.id == place_id, PlaceBook.id == book_id)
    res = [i.to_hash() for i in book_query]

    if res:
        return jsonify(res)

    output = {'error': 'No results found'}
    res = jsonify(output)
    res.status_code = 404
    return res


@app.route('/places/<place_id>/books/<book_id>', methods=['PUT'])
def update_book_by_id(place_id, book_id):

    book_query = PlaceBook.select().join(Place).where(PlaceBook.id == book_id, Place.id == place_id).get()

    for key in request.values.keys():
        if key == 'is_validated':
            book_query.is_validated = request.values[key]
        elif key == 'date_start':
            book_query.date_start = request.values[key]
        elif key == 'number_nights':
            book_query.number_nights = request.values[key]
        elif key == 'user_id' or key == 'place_id':
            output = {'error': key + ' Not accepted'}
            error = jsonify(output)
            error.status_code = 400
            return error

    book_query.save()
    return jsonify(book_query.to_hash())


@app.route('/places/<place_id>/books/<book_id>', methods=['DELETE'])
def delete


'''
route /places/<place_id>/books/<book_id>:
DELETE: delete book with id = book_id
'''
