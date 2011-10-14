from fabric.api import *

def create_working_copy(name):
    print "{FABRIC} install working copy for %s" % name

def create_db(name):
    print "{FABRIC} create database for %s" % name
    
def setup_services(name):
    print "{FABRIC} setup services for %s" % name
     
     
steps_for_create = [create_working_copy,
                    create_db,
                    setup_services]
@task
def create_branch(name):
    launch_steps(steps_for_create, name)
    
def launch_steps(steps, name):
    for step in steps:
        step(name)
    

     
