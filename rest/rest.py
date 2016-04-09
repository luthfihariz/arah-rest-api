import os
from dbconfig import db
from flask import Flask, make_response
from flask.ext.restful import Api
from bson.json_util import dumps
from nearby import nearby_api, NearbyPublicTransportApi


app = Flask(__name__)
app.register_blueprint(nearby_api)
api = Api(app)

def toJson(obj, code, headers=None):
	resp = make_response(dumps(obj), code)
	resp.headers.extend(headers or {})
	return resp

#API Mapping
api_version = '1';
api.representations = {'application/json':toJson}
api.add_resource(NearbyPublicTransportApi, "/v{}/transport/nearby".format(api_version))


@app.route('/')
def hello():
    return 'Hello Rest World!'

@app.route('/testdb')
def testdb():
	query = db['public_transport_route'].find()
	return "There are {} routes stored in database. Have fun!".format(query.count())

if __name__ == "__main__":
    app.run(debug=True)