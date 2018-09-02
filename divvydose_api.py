from flask import Flask
from github import Github
import requests
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

g = Github()
user = requests.get('https://api.github.com/users/kennethreitz')
repos = requests.get('https://api.github.com/repos')
total = user.json()

bitbucket = requests.get('https://api.bitbucket.org/2.0/users/tutorials')


class HelloWorld(Resource):
    def get(self):
        return {'hello': total["public_repos"], "bitbucket":bitbucket.json(),"forks":repos.json() }


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)