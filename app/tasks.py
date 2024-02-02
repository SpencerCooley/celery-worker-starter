# app/tasks.py
from dotenv import load_dotenv
import os
import sys
from celery import Celery
load_dotenv()

# Access environment variables
rabbit_user = os.environ['RABBIT_USER']
rabbit_pass = os.environ['RABBIT_PASS']
rabbit_host = os.environ['RABBIT_HOST']

# set up celery with credentials
celery = Celery('tasks',
                broker=f'pyamqp://{rabbit_user}:{rabbit_pass}@{rabbit_host}//',
                include=['tasks'])

# Define Celery tasks here
@celery.task
def print_something(arg1, arg2):
    # Task implementation
    print("this is working")
    print(arg1)
    print(arg2)
    pass

@celery.task
def print_something(arg1, arg2):
    # Task implementation
    print("this is working")
    print(arg1)
    print(arg2)
    pass


# add tasks for whatever you want to do without blocking the api
# run ml models, 
# process large files 
# send emails, text
# make scheduled tasks
# do whatever