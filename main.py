import config
import logging
from flask import Flask, json, abort
from models import db, Parent, Child

app = Flask (__name__)
app.config.from_object (config)

db.init_app (app)

@app.route ('/', methods = ['GET'])
def index ():
    p = Parent (ema = 'a@somewhere.com', nam = 'Andy Testing Parent')
    p.children.append (Child (nam = 'Mary Testing Child'))

    print (p)
    print (p.serialize ())

    try:
        db.session.add (p)
        db.session.commit ()
        return json.jsonify (p.serialize ())

    except Exception as e:
        db.session.rollback ()
        abort (500, 'Error. Something bad happened.')


if __name__ == '__main__':
    # Note: Ensure that all appropriate tables are created in the production database before deploying.
    with app.app_context ():
        db.drop_all ()
        db.create_all ()

    app.run (
        host = '127.0.0.1',
        port = 8080,
        debug = True,
    )
