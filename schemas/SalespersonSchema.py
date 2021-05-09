from main import ma
from models.Salesperson import Salesperson
from marshmallow.validate import Length
from schemas.RegionSchema import RegionSchema
from marshmallow import Schema, fields

class SalespersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Salesperson

    name = ma.String(required=True, validate=Length(min=1))
    email = ma.String(required=True, validate=Length(min=1))
    region_id = ma.String(required=True, validate=Length(min=1))
    region_name = ma.String(required=True, validate=Length(min=1))
    
salesperson_schema = SalespersonSchema()
salespersons_schema = SalespersonSchema(many=True)