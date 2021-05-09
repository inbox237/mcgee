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
    from models.Region import Region
    from models.Salesperson import Salesperson
    from faker import Faker
    faker = Faker()
    
    #Mcgee
    for i in range(20):
        states = ["NSW", "QLD", "SA", "TAS", "VIC", "WA", "ACT", "NT"]
        office = Office()
        office.name = (random.choice(states))
        db.session.add(office)

    db.session.commit()

    for i in range(20):
        agent = Agent()
        namesplit = faker.name().split(" ")
        
        agent.first_name = namesplit[0]
        agent.last_name = namesplit[1]
        agent.email = f"{namesplit[0]}{namesplit[1]}@mcgee.com"
        agent.office_id = random.randint(1,20)

        db.session.add(agent)

    #May Black
    for i in range(20):
        states = ["NSW", "QLD", "SA", "TAS", "VIC", "WA", "ACT", "NT"]
        region = Region()
        region.name = (random.choice(states))
        db.session.add(region)

    db.session.commit()

    for i in range(20):
        salesperson = Salesperson()
        namenonsplit = faker.name()
        namesplit = faker.name().split(" ")
        
        salesperson.name = f"{namesplit[0]}{namesplit[1]}"
        salesperson.email = f"{namesplit[0]}{namesplit[1]}@mcgee.com"
        salesperson.region_id = random.randint(1,20)

        db.session.add(salesperson)


    db.session.commit()

    print("Tables seeded")