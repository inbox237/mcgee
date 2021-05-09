from models.Salesperson import Salesperson
from main import db
from schemas.SalespersonSchema import salesperson_schema, salespersons_schema
from flask import Blueprint, request, jsonify, abort
salespersons = Blueprint('salespersons', __name__, url_prefix="/salespersons")

@salespersons.route("/", methods=["GET"])
def salesperson_index():
    #Retrieve all salespersons
    salespersons = Salesperson.query.all()
    return jsonify(salespersons_schema.dump(salespersons))

@salespersons.route("/", methods=["POST"])
def salesperson_create():
    #Create a new salesperson
    salesperson_fields = salesperson_schema.load(request.json)

    new_salesperson = Salesperson()
    new_salesperson.name = salesperson_fields["name"]
    
    db.session.add(new_salesperson)
    db.session.commit()
    
    return jsonify(salesperson_schema.dump(new_salesperson))

@salespersons.route("/<int:id>", methods=["GET"])
def salesperson_show(id):
    #Return a single salesperson
    salesperson = Salesperson.query.get(id)

    if not salesperson:
        return abort(404, description="Invalid Salesperson ID" )

    return jsonify(salesperson_schema.dump(salesperson))

