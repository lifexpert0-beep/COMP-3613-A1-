import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import (Student,Staff,ServiceEntry)
from App.main import create_app
from App.controllers import ( initialize )
from App.controllers import ( create_student,get_all_students, create_staff,create_request,view_all_requests,log_hours)


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    
    initialize()
    print('database intialized')

'''
Student Commands
'''
#Student Account Creation

student_cli = AppGroup('student', help='Student object commands') 
@student_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
def create_user_command(username):
    new_student=create_student(username)
    studentid=new_student.studentid
    print(f'{username} created!, Your ID is {studentid}')

#View All Students (my personal use)
@student_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_student_command(format):
        print(get_all_students())
#Student View Accolades
#Student View LeaderBoards
#Student Request Hours
@student_cli.command("request", help="Request hours from staff")
@click.argument("studentid", type=int)
@click.argument("hours", type=int)
def requestHours(studentid,hours):
    create_request(studentid,hours)
    print(f'Your request for {hours} hours of service for student {studentid} has been forwarded to staff.')

app.cli.add_command(student_cli)

'''
Staff Commands
'''

#Staff Create Account

staff_cli = AppGroup('staff', help='Staff object commands')
@staff_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
def create_staff_command(username):
    new_staff=create_staff(username)
    staffid=new_staff.staffid
    print(f'{username} created!, Your ID is {staffid}')

#Staff Log Hours

@staff_cli.command("log", help="Log community service hours for students")
@click.argument("staffid",type=int)
@click.argument("serviceid",type=int)
@click.argument("status",type=int) # 0/1 = Approved/Rejected
def log_hours_command(staffid,serviceid,status):
    log_hours(staffid,serviceid,status)
    if(status==0):
         print(f'You have approved service ticket {serviceid}.')
    elif (status==1): 
         print(f'You have rejected service ticket {serviceid}.')
    else:
         print(f'You have entered an invalid option. Syntax = StaffID ServiceID,Status [0/1 = Approved/Rejected]')
#Staff View Pending confirms

@staff_cli.command("view", help="View Requests for community service hours")
@click.argument("format", default="string")
def list_student_command(format):
        print(view_all_requests())
        
app.cli.add_command(staff_cli)