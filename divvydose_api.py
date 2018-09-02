from flask import Flask
from github import Github
import requests
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

g = Github()
user = requests.get('https://api.github.com/users/kennethreitz')
watchers = requests.get('https://api.github.com/users/kennethreitz/subscriptions')
stars = requests.get('https://api.github.com/users/kennethreitz/starred')
stars_given = requests.get('http://api.github.com/users/starred/kennethreitz/repo')
repos = requests.get('https://api.github.com/repos')
total = user.json()

bitbucket = requests.get('https://api.bitbucket.org/2.0/users/tutorials')


class HelloWorld(Resource):
    def get(self):
        return {'data': total["public_repos"],
        "bitbucket":bitbucket.json(), 
        "forks":repos.json(), 
        "watchers":watchers.json(),
        "stars":stars.json(),
        "stars-given":stars_given.json()
        }


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)