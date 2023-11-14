from flask import Flask
from flask_restful import Api, Resource  # Resource is a class

app = Flask(__name__)
api = Api(app)

names = {"tim": {"age": 29, "gender": "male"},
         "bill": {"age": 54, "gender": "male"}}


class HelloWorld(Resource):
    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)
