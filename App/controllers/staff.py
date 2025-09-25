from App.database import db
from App.models import Staff

def create_staff(username):
    newuser = Staff(username=username)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_all_students():
    return db.session.scalars(db.select(Staff)).all()