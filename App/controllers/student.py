from App.database import db
from App.models import Student

def create_student(username):
    newuser = Student(username=username)
    db.session.add(newuser)
    db.session.commit()
    return newuser
def get_all_students():
    return db.session.scalars(db.select(Student)).all()