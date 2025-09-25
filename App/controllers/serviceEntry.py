from App.database import db
from App.models import ServiceEntry as ServiceModel 

def create_request(studentid,hours):
    newrequest = ServiceModel(studentid=studentid,hours=hours)
    db.session.add(newrequest)
    db.session.commit()
    return newrequest

def view_all_requests():
    pendingrequests= db.select(ServiceModel)
    pendingrequests = pendingrequests.where(ServiceModel.status == 2)
    return db.session.scalars(pendingrequests).all()

def log_hours(staffid,serviceid,status):
    if(status == 0):
        log = db.session.get(ServiceModel,serviceid)
        log.staff_id = staffid
        log.status = status
        db.session.add(log)
        db.session.commit()

        return log 
    elif (status == 1):
        log = db.session.get(ServiceModel,serviceid)
        log.staff_id = staffid
        log.status = status
        db.session.add(log)
        db.session.commit()
        return
    else:
        return 
    