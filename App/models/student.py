from App.database import db

class Student(db.Model):
    studentid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    hours = db.Column(db.Integer, default=0)

    def __init__(self, username):
        self.username = username
        self.hours = 0

    def __repr__(self):
        return f'<{self.username} - {self.studentid}>'
