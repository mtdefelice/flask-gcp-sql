import logging
from flask import abort, json
from app import app, db, models

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


@app.route ('/del', methods = ['GET'])
def dd ():
    p = models.Parent.query.first ()
    if p:
        try:
            db.session.delete (p)
            db.session.commit ()
            return '''Done.'''

        except Exception as e:
            print (e)
            logging.error (e.__class__.__name__)
            db.session.rollback ()
            abort (500, 'Error. Something bad happened.')
    else:
        return '''N/A'''

