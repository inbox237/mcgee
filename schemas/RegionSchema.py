from main import ma
from models.Region import Region
from marshmallow.validate import Length

class RegionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Region

    name = ma.String(required=True, validate=Length(min=1))
    
    
region_schema = RegionSchema()
regions_schema = RegionSchema(many=True)