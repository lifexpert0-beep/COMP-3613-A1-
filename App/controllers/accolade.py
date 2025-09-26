from App.database import db
from App.models import Accolade

def get_all_accolades():
    return db.session.scalars(db.select(Accolade)).all()