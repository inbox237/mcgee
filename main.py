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
POOL_TIME = 5 #Seconds

# variables that are accessible from anywhere
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
                    salesperson_query = db.session.query(Salesperson).filter(Salesperson.region_id==2)
                    for salesperson in salesperson_query:
                        agent_query = db.session.query(Agent).filter(Agent.email==salesperson.email)
                        print(list(agent_query))
                        if len(list(agent_query))==0:
                            first_name, last_name = salesperson.name.split(" ")
                            agent = Agent(first_name=first_name, last_name=last_name, email=salesperson.email, office_id=salesperson.region_id)
                            db.session.add(agent)
                    db.session.commit()
                    bg_worker = threading.Timer(POOL_TIME, background_update, ())
                    bg_worker.start() 
                except (NameError, exc.ProgrammingError, NoResultFound):
                    return  


    #NOT NEEDED BUT MAY BE USEFUL LATER
    def background_update_start():
        # Do initialisation here
        global bg_worker
        
        # Create your thread
        with app.app_context():
            try:
                salesperson_query = db.session.query(Salesperson).filter(Salesperson.region_id==2)
                print(list(salesperson_query))
                if not len(list(salesperson_query)): #is empty
                    return
            except (NameError, exc.ProgrammingError, NoResultFound):
                return
        bg_worker = threading.Timer(POOL_TIME, background_update, ())
        bg_worker.start()

    # Initiate
    background_update_start()
    
    return app








    