from flask import Flask, render_template
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from config import config
from db import db
import os

from resources.accounts import Accounts
from resources.match import Match
from resources.login import Login


app = Flask(
    __name__,
    static_folder="frontend/dist/static",
    template_folder="frontend/dist"
)

environment=  config['development']
if os.environ.get('PRODUCTION') == 'true':
    environment = config['production']

app.config.from_object(environment)

api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Migrate(app, db)



api.add_resource(Login, "/login")
api.add_resource(Accounts, "/account/<string:username>", "/account")

api.add_resource(Match, "/match/<int:id>", "/match")

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
