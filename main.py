import threading
import atexit

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify, request, current_app, session
from marshmallow.exceptions import ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import exc
from sqlalchemy.orm.exc import NoResultFound
import psycopg2



db = SQLAlchemy()
ma = Marshmallow()

#BACKGROUND WORKER - GLOBAL
POOL_TIME = 60 #Seconds

# accessible from anywhere
commonDataStruct = {}
# lock to control access to variable
dataLock = threading.Lock()
# thread handler
bg_worker = threading.Thread()

def create_app():

    app = Flask(__name__)
    app.config.from_object("default_settings.app_config")

    db.init_app(app)
    ma.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages), 400)


#Encountering an error: "RuntimeError: No application found. Either work inside a view function or push an application context"
# Attempted solutions to this error I have tried (putting these ahead of the background worker details below):
    #app.app_context().push()
    #with app.app_context():
    #with app.config.from_object("default_settings.app_config"):
    # > the solution was to put the 'app.app_context().push()' inside the background update function :), spent a lot of time on this.
  
    
    #BACKGROUND WORKER MAIN CODE
    from models.Salesperson import Salesperson
    from models.Agent import Agent

    def background_update():
        global commonDataStruct
        global bg_worker
        with dataLock:
            with app.app_context():
                try:
                    salesperson_query = db.session.query(Salesperson).filter(Salesperson.region_id==2) #finds all salespersons that have region id of 2 which is QLD
                    updated = False
                    print('Comparing McGee and Mayblack databases...')
                    for salesperson in salesperson_query:
                        agent_query = db.session.query(Agent).filter(Agent.email==salesperson.email) #finds all salespersons that already exist in agents matched on email
                        if len(list(agent_query))==0:#makes the above into a list and if len = 0 it means it already exists and doesnt add, otherwise add
                            first_name, last_name = salesperson.name.split(" ")
                            agent = Agent(first_name=first_name, last_name=last_name, email=salesperson.email, office_id=salesperson.region_id)
                            db.session.add(agent)
                            updated = True
                    db.session.commit()
                    print('Differences in databases found, update completed, sleeping...') if updated else print('Nothing found to update, sleeping...')
                    bg_worker = threading.Timer(POOL_TIME, background_update, ())
                    bg_worker.start()
                except (NameError, exc.ProgrammingError, NoResultFound):
                    return 
    
    def background_update_start():
        # initialisation
        global bg_worker
        
        # Had to move this section down here in separate try except as it was causing issues with seed and drop, this prevents a worker starting if query finds no salespeople matching
        with app.app_context():
            try:
                salesperson_query = db.session.query(Salesperson).filter(Salesperson.region_id==2)
                if not len(list(salesperson_query)): #is empty, falsey interaction
                    return
            except (NameError, exc.ProgrammingError, NoResultFound):
                return
        bg_worker = threading.Timer(5, background_update, ()) #timer is time before start worker
        bg_worker.start()

    # Initiate
    background_update_start()
    
    return app








    