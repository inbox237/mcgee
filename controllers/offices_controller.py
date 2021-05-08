from models.Office import Office
from main import db
from schemas.OfficeSchema import office_schema, offices_schema
from flask import Blueprint, request, jsonify, abort
offices = Blueprint('offices', __name__, url_prefix="/offices")

@offices.route("/", methods=["GET"])
def office_index():
    #Retrieve all offices
    offices = Office.query.all()
    return jsonify(offices_schema.dump(offices))

@offices.route("/", methods=["POST"])
def office_create():
    #Create a new office
    office_fields = office_schema.load(request.json)

    new_office = Office()
    new_office.name = office_fields["name"]
    
    db.session.add(new_office)
    db.session.commit()
    
    return jsonify(office_schema.dump(new_office))

@offices.route("/<int:id>", methods=["GET"])
def office_show(id):
    #Return a single office
    office = Office.query.get(id)

    if not office:
        return abort(400, description="Invalid Office ID" )

    return jsonify(office_schema.dump(office))

