import os
from flask import Flask
from dbconfig import db

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Rest World!'

@app.route('/testdb')
def testdb():
	query = db['public_transport_route'].find()
	return "There are {} routes stored in database. Have fun!".format(query.count())

if __name__ == "__main__":
    app.run()