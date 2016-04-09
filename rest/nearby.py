from flask import Blueprint
from flask.ext.restful import reqparse, Resource
from dbconfig import db

nearby_api = Blueprint('nearbyApi',__name__)
parser = reqparse.RequestParser()

class NearbyPublicTransportApi(Resource):

	def __init__(self):
		parser.add_argument('lat', type=float)
		parser.add_argument('lng', type=float)
		parser.add_argument('radius', type=float)
		parser.add_argument('order', type=int)
		parser.add_argument('limit', type=int)
		parser.add_argument('skip', type=int)
		super(NearbyPublicTransportApi, self).__init__()

	def get(self):
		args = parser.parse_args()
		lat = args['lat']
		lng = args['lng']
		radius = args['radius']
		order = args['order']
		limit = args['limit']	
		skip = args['skip']

		radius = radius if radius else 1000
		order = order if order else 1
		limit = limit if limit else 5
		skip = skip if skip else 0
		radians = radius/float(6371000)

		queryResult = db.public_transport_route.aggregate([
			{'$geoNear': {
				'near': [lng, lat],
				'distanceField': 'distance',
				'distanceMultiplier': 6371,
				'spherical': True,
				'maxDistance': radians,
				'limit': limit,
				}
			},
		])

		result = {'status' : True, 'result' : queryResult}
		return result;
