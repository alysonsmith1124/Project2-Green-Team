import pandas as pd 

from flask import Flask, jsonify, render_template

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///spotify.sqlite"

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)
# Save references to each table
Tracks = Base.classes.tracks
Features = Base.classes.features

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/tracks")
def tracks():
    stmt = db.session.query(Tracks).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    return jsonify(df)

if __name__ == "__main__":
    app.run(debug=True)

