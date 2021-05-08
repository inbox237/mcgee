###from controller:

# @offices.route("/<int:id>", methods=["PUT", "PATCH"])
# def office_update(id):
#     #Update a office
#     offices = Book.query.filter_by(id=id)
#     office_fields = office_schema.load(request.json)
#     offices.update(office_fields)
#     db.session.commit()

#     return jsonify(office_schema.dump(offices[0]))

# @offices.route("/<int:id>", methods=["DELETE"])
# def office_delete(id):
#     #Delete a office
#     office = Book.query.get(id)
#     db.session.delete(office)
#     db.session.commit()

#     return jsonify(office_schema.dump(office))


#DB_BINDS = {"mayblack":"postgresql+psycopg2://postgres:coder@13.210.56.56/mcgee_mayblack"}