from App.database import db

class Accolade(db.Model):

    accoladeid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    hoursrequired = db.Column(db.Integer)

    def __init__(self, title,description,hoursrequired):
        self.title = title
        self.description = description
        self.hoursrequired = hoursrequired

    def __repr__(self):
        return f'< Hours Required : {self.hoursrequired} - Title: {self.title} - Benefit: {self.description}>'