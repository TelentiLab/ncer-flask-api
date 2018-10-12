from flask import Flask
from flask_restful import Api
import os

from db import db
from resources.ncer import Ncer

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = os.getenv("SECRET_KEY")
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Ncer, "/ncer/<string:chrom>/<int:start>/<int:end>")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
