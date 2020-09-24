from flask import Flask 
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

a_language = api.model('Language', {'language' : fields.String('The language.')})

languages = []
python = {'language' : 'Python'}
languages.append(python)

ns_conf = api.namespace('language', description='Programmig language operations')

@ns_conf.route('/')
class Language(Resource):
    def get(self):
        return languages

    @api.expect(a_language)
    def post(self):
        languages.append(api.payload)
        return {'result' : 'Language added'}, 201 

if __name__ == '__main__':
    app.run(debug=True)