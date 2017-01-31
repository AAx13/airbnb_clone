from app import app
from flask_json import jsonify
from app.models.amenity import Amenity
from app.models.place_amenity import PlaceAmenities

@app.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity_by_id(amenity_id):

    amenity_query = Amenity.get(Amenity.id == amenity_id)
    return jsonify(amenity_query.to_hash())


@app.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity_by_id(amenity_id):

    amenity_query = Amenity.get(Amenity.id == amenity_id)
    amenity_query.delete_instance()
    amenity_query.save()
    response = {'msg': 'deleted amenity at id: ' + amenity_id}
    return jsonify(response)


@app.route('/places/<place_id>/amenities', methods=['GET'])
def get_amenities_from_place(place_id):

    amenity_query = Amenity.select().join(PlaceAmenities).where(PlaceAmenities.place == place_id)
    res = [i.to_hash() for i in amenity_query]

    if res:
        jsonify(res)

    output = {'error': 'No results found'}
    res = jsonify(output)
    res.status_code = 404
    return res
