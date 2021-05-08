from models.Agent import Agent
from main import db
from schemas.AgentSchema import agent_schema, agents_schema
from flask import Blueprint, request, jsonify, abort
agents = Blueprint('agents', __name__, url_prefix="/agents")

@agents.route("/", methods=["GET"])
def agent_index():
    #Retrieve all agents
    agents = Agent.query.all()
    return jsonify(agents_schema.dump(agents))

@agents.route("/", methods=["POST"])
def agent_create():
    #Create a new agent
    agent_fields = agent_schema.load(request.json)

    new_agent = Agent()
    new_agent.name = agent_fields["name"]
    
    db.session.add(new_agent)
    db.session.commit()
    
    return jsonify(agent_schema.dump(new_agent))

@agents.route("/<int:id>", methods=["GET"])
def agent_show(id):
    #Return a single agent
    agent = Agent.query.get(id)

    if not agent:
        return abort(400, description="Invalid Agent ID" )

    return jsonify(agent_schema.dump(agent))

