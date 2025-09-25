from App.database import db

class Staff(db.Model):
    staffid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username):
        self.username = username
    def __repr__(self):
        return f'<{self.username} - {self.staffid}>'
        
    
        