from main import ma
from models.Office import Office
from marshmallow.validate import Length

class OfficeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Office

    name = ma.String(required=True, validate=Length(min=1))
    
    
office_schema = OfficeSchema()
offices_schema = OfficeSchema(many=True)