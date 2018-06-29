from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy ()

class Parent (db.Model):
    pid = db.Column (db.Integer, primary_key = True)
    ema = db.Column (db.String (255), nullable = False, unique = True)
    nam = db.Column (db.String (255), nullable = False)

    children = db.relationship ('Child', backref = 'parent', lazy = True)

    def serialize (self):
        return {
            'pid': self.pid,
            'ema': self.ema,
            'nam': self.nam,
            'children': [ a.serialize () for a in self.children ],
        }

    def __repr__ (self):
        return '<Parent {}>'.format (self.ema)


class Child (db.Model):
    cid = db.Column (db.Integer, primary_key = True)
    nam = db.Column (db.String (255), nullable = False)

    parent_pid = db.Column(db.Integer, db.ForeignKey ('parent.pid'), nullable = False)
    
    def serialize (self):
        return {
            'cid': self.cid,
            'nam': self.nam,
        }

    def __repr__ (self):
        return '<Child {}>'.format (self.nam)


def _create_database ():
    """
    Run this script directly before deploying to production to create all of the necessary tables.
    """

    import config
    from flask import Flask

    app = Flask (__name__)
    app.config.from_object (config)

    db.init_app (app)

    with app.app_context ():
        db.drop_all ()
        db.create_all ()

if __name__ == '__main__':
    _create_database ()

