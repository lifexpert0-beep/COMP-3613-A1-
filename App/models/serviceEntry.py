from App.database import db

class ServiceEntry(db.Model):

    serviceid = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.studentid"), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey("staff.staffid"), nullable=True)
    hours = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, unique=False, default=2)

    # relationships declared only here
    student = db.relationship('Student', backref=db.backref('logs', lazy=True))
    staff = db.relationship('Staff', backref=db.backref('logged_hours', lazy=True))

    def __init__(self, studentid, hours):
        self.student_id = studentid
        self.hours = hours
        
    def __repr__(self):
        return f'<Service Ticket {self.serviceid} - Student ID: {self.student_id} - Hours Requested: {self.hours}>'
    