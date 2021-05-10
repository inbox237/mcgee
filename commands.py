from main import db
from flask import Blueprint, current_app
from flask.cli import with_appcontext
import random
import click
from click import pass_context
import webbrowser
import os
import subprocess

REGION_NAMES = {
        1: "NSW",
        2: "QLD",
        3: "SA",
        4: "TAS",
        5: "VIC",
        6: "WA",
        7: "ACT",
        8: "NT"}
db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.Office import Office
    from models.Agent import Agent
    from models.Region import Region
    from models.Salesperson import Salesperson
    from faker import Faker

    faker = Faker()
    
    #Mcgee Real Estate Seeds
    for i in range(1,9):
        office = Office()
        office.name = REGION_NAMES[i]
        db.session.add(office)

    db.session.commit()

    for i in range(20):
        agent = Agent()
        namesplit = faker.name().split(" ")
        
        agent.first_name = namesplit[0]
        agent.last_name = namesplit[1]
        agent.email = f"{namesplit[0]}{namesplit[1]}@mcgee.com"
        agent.office_id = random.randint(1,8)

        db.session.add(agent)

    #Decided to use set region ids instead
    #May Black Real Estate Seeds
    # for i in range(20):
    #     states = ["NSW", "QLD", "SA", "TAS", "VIC", "WA", "ACT", "NT"]
    #     region = Region()
    #     region.name = (random.choice(states))
    #     db.session.add(region)

    for i in range(1, 9):
        region = Region()
        

        region.name = REGION_NAMES[i]
        db.session.add(region)


    db.session.commit()

    for i in range(20):
        salesperson = Salesperson()
        namenonsplit = faker.name()
        namesplit = faker.name().split(" ")
        
        #Faker sometimes returned more than two words for a name - workaround
        salesperson.name = f"{namesplit[0]} {namesplit[1]}"

        salesperson.email = f"{namesplit[0]}{namesplit[1]}@mcgee.com"
        salesperson.region_id = random.randint(1,8)

        db.session.add(salesperson)


    db.session.commit()

    print("Tables seeded")


@db_commands.cli.command("start")
@pass_context
def refresh_db(ctx):
    drop_db.invoke(ctx)
    create_db.invoke(ctx)
    seed_db.invoke(ctx)
    print("All Done! A web browser will launch showing the final list of agents....")
    webbrowser.open("http://127.0.0.1:5000/agents/")
    os.system("FLASK_DEBUG=1 flask run --no-reload")
    # subprocess.Popen(["FLASK_DEBUG=1", "flask", "run", "--no-reload"]) tried to use to create non-blocking process so the web browser can be opened after update
    # but permissions error needs to be corrected.