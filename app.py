import pandas as pd 
import os
from flask import Flask, jsonify, render_template, g

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlite3

from flask_sqlalchemy import SQLAlchemy 



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///spotify.sqlite"

db = SQLAlchemy(app)

# from .models import Songs, Features

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












# reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)
# # Save references to each table
# songs = Base.classes.artists_songs
# analyzed = Base.classes.artists_songs_analyzed

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/tracks")
def tracks():
    results = db.session.query(Songs.Song).all()
    results2 = results[0:100]

    return jsonify(results2)


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

        #if sample_metadata in sample_metadata:
            #sample_metadata[sample].append(result[0])
        #else:
            #sample_metadata[sample] = [result[0]]


        #sample_metadata.append(result)
    print(feature_dict)
    return jsonify(feature_dict)

@app.route("/alltrackfeatures")
def alltrackfeatures():
    """Return the MetaData for a given sample."""
 
    # conn = sqlite3.connect("sqlite:///spotify.sqlite")
    # conn.row_factory = sqlite3.Row
    # c = conn.cursor()
    # c.execute('select * from artists_songs_analyzed')

    # total_info = c.fetchall()
    
     
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
    

   






    
  
    print(results5)
    # df4 = pd.DataFrame(results5)
    # test1 = df4.to_dict()


       #sample_metadata.append(result)
    #print(feature_dict)
    return jsonify(master_list)





if __name__ == "__main__":
    app.run(debug=True)