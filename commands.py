from main import db
from flask import Blueprint
import random

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
    from faker import Faker
    faker = Faker()
    

    for i in range(20):
        states = ["NSW", "QLD", "SA", "TAS", "VIC", "WA", "ACT", "NT"]
        office = Office()
        office.name = (random.choice(states))
        db.session.add(office)

    db.session.commit()

    for i in range(20):
        agent = Agent()

        agent.first_name = random.randint(21,40)
        agent.last_name = random.randint(21,40)
        agent.email = random.randint(21,40)
        agent.office_id = random.randint(1,20)
        #agent.office_name = random.randint(1,20)

        db.session.add(agent)

    db.session.commit()

    print("Tables seeded")