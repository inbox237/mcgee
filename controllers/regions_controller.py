from models.Region import Region
from main import db
from schemas.RegionSchema import region_schema, regions_schema
from flask import Blueprint, request, jsonify, abort
regions = Blueprint('regions', __name__, url_prefix="/regions")

@regions.route("/", methods=["GET"])
def region_index():
    #Retrieve all regions
    regions = Region.query.all()
    return jsonify(regions_schema.dump(regions))

@regions.route("/", methods=["POST"])
def region_create():
    #Create a new region
    region_fields = region_schema.load(request.json)

    new_region = Region()
    new_region.name = region_fields["name"]
    
    db.session.add(new_region)
    db.session.commit()
    
    return jsonify(region_schema.dump(new_region))

@regions.route("/<int:id>", methods=["GET"])
def region_show(id):
    #Return a single region
    region = Region.query.get(id)

    if not region:
        return abort(404, description="Invalid Region ID" )

    return jsonify(region_schema.dump(region))

