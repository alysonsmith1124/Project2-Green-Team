# import our libraries
import pandas as pd 
import os
from flask import Flask, jsonify, render_template, g

# import SQLAchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlite3
from flask_sqlalchemy import SQLAlchemy 

# set up Flask app and link to database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///spotify.sqlite"
db = SQLAlchemy(app)

# create classes to format tables and map database info to
class Songs(db.Model):
    __tablename__ = 'artists_songs'

    Artist = db.Column(db.String)
    Song = db.Column(db.String, primary_key=True)
    
    def __repr__(self):
        return '<Songs %r>' % (self.Artist)


class Features(db.Model):
    __tablename__ = 'artists_songs_analyzed'

    Artist = db.Column(db.String)   
    Song = db.Column(db.String, primary_key=True)     
    acousticness = db.Column(db.Float)   
    analysis_url = db.Column(db.String)     
    danceability = db.Column(db.Float)   
    duration_ms = db.Column(db.Float)   
    energy = db.Column(db.Float)   
    id = db.Column(db.String)     
    instrumentalness = db.Column(db.Float)   
    key = db.Column(db.Integer)   
    liveness = db.Column(db.Float)   
    loudness = db.Column(db.Float)   
    mode = db.Column(db.Integer)   
    speechiness = db.Column(db.Float)   
    tempo = db.Column(db.Float)   
    time_signature = db.Column(db.Integer)   
    track_href = db.Column(db.String)     
    type = db.Column(db.String)     
    uri = db.Column(db.String)     
    valence = db.Column(db.Float)
  

    def __repr__(self):
        return '<Features %r>' % (self.Artist)

#Flask app routes
#route to render app templete from index.html
@app.route("/")
def index():
    return render_template('index.html')

#route to return jsonified song list
@app.route("/tracks")
def tracks():
    results = db.session.query(Songs.Song).all()
    results2 = results[0:100]

    return jsonify(results2)

#route to return jsonified track features for specific song
@app.route("/trackfeatures/<song>")
def trackfeatures(song):
    """Return the MetaData for a given sample."""
   
    sel = [
        Features.Artist,
        Features.Song,
        Features.acousticness,
        Features.analysis_url,
        Features.danceability,
        Features.duration_ms,
        Features.energy,
        Features.id,
        Features.instrumentalness,
        Features.key,
        Features.liveness,
        Features.loudness,
        Features.mode,
        Features.speechiness,
        Features.tempo,
        Features.time_signature,
        Features.track_href,
        Features.type,
        Features.uri,
        Features.valence
    ]
   
    results = db.session.query(*sel).filter(Features.Song==song).all()

    feature_dict = {}

    for result in results:
        feature_dict["Artist"] = result[0]
        feature_dict["Song"] = result[1]
        feature_dict["acousticness"] = result[2]
        feature_dict["analysis_url"] = result[3]
        feature_dict["danceability"] = result[4]
        feature_dict["duration_ms"] = result[5]
        feature_dict["energy"] = result[6]
        feature_dict["id"] = result[7]
        feature_dict["instrumentalness"] = result[8]
        feature_dict["key"] = result[9]
        feature_dict["liveness"] = result[10]
        feature_dict["loudness"] = result[11]
        feature_dict["mode"] = result[12]
        feature_dict["speechiness"] = result[13]
        feature_dict["tempo"] = result[14]
        feature_dict["time_signature"] = result[15]
        feature_dict["track_href"] = result[16]
        feature_dict["type"] = result[17]
        feature_dict["uri"] = result[18]
        feature_dict["valence"] = result[19]

        print(feature_dict)
    return jsonify(feature_dict)

#route to return jsonified features for all songs
@app.route("/alltrackfeatures")
def alltrackfeatures():

    #Return the MetaData for a given sample  
    sel = [
        Features.Artist,
        Features.Song,
        Features.acousticness,
        Features.analysis_url,
        Features.danceability,
        Features.duration_ms,
        Features.energy,
        Features.id,
        Features.instrumentalness,
        Features.key,
        Features.liveness,
        Features.loudness,
        Features.mode,
        Features.speechiness,
        Features.tempo,
        Features.time_signature,
        Features.track_href,
        Features.type,
        Features.uri,
        Features.valence
    ]
   
    results5 = db.session.query(*sel).filter().all()



    list_of_keys = ["Artist",
        "Song",
        "acousticness",
        "analysis_url",
        "danceability",
        "duration_ms",
       "energy",
        "id",
        "instrumentalness",
        "key",
        "liveness",
        "loudness",
        "mode",
        "speechiness",
        "tempo",
        "time_signature",
       "track_href",
        "type",
        "uri",
        "valence"]

    # loop through query results to format into correct format and jsonified 
    # the final list
    list_of_values = []
    data = {}
    master_list = []

    for result in results5:
        for j in range(0,20):
            list_of_values.append(result[j])
        data = dict(zip(list_of_keys, list_of_values))
        master_list.append(data)
        data = {}
        list_of_values = []

    return jsonify(master_list)



if __name__ == "__main__":
    app.run(debug=True)