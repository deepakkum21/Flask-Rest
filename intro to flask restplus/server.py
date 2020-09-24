from flask import Flask
from flask_restplus import Api, Resource
app = Flask(__name__)
api = Api(app=app)
@api.route("/conferences/")
class ConferenceList(Resource):
    def get(self):
        """
        returns a list of conferences
        """
    def post(self):
        """
        Adds a new conference to the list
        """
@api.route("/conferences/<int:id>")
class Conference(Resource):
    def get(self, id):
        """
        Displays a conference's details
        """
    def put(self, id):
        """
        Edits a selected conference
        """

if __name__ == '__main__':
    app.run(debug=True)        