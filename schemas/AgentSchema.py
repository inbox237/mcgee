from main import ma
from models.Agent import Agent
from marshmallow.validate import Length
from schemas.OfficeSchema import OfficeSchema
from marshmallow import Schema, fields

class AgentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Agent

    first_name = ma.String(required=True, validate=Length(min=1))
    last_name = ma.String(required=True, validate=Length(min=1))
    email = ma.String(required=True, validate=Length(min=1))
    office_id = ma.String(required=True, validate=Length(min=1))
    office_name = ma.String(required=True, validate=Length(min=1))
    
agent_schema = AgentSchema()
agents_schema = AgentSchema(many=True)