import config
import logging
from flask import Flask, json, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config.from_object (config)

db = SQLAlchemy (app)
import models

@app.route ('/', methods = ['GET'])
def index ():
    p = models.Parent.query.first ()
    if p:
        return json.jsonify (p.serialize ())
    else:
        p = models.Parent (ema = 'a@somewhere.com', nam = 'Andy Testing Parent')
        p.children.append (models.Child (nam = 'Mary Testing Child'))
        p.children.append (models.Child (nam = 'Jane Testing Child'))
        p.children.append (models.Child (nam = 'Sara Testing Child'))

        try:
            db.session.add (p)
            db.session.commit ()
            return json.jsonify (p.serialize ())

        except Exception as e:
            logging.error (e.__class__.__name__)
            db.session.rollback ()
            abort (500, 'Error. Something bad happened.')

if __name__ == '__main__':
    app.run (
        host = '127.0.0.1',
        port = 8080,
        debug = True,
    )
