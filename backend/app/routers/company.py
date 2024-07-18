from flask import Blueprint, jsonify, request
from app.models.company import Company
from app.models.user import User
from app.config import db


company_router = Blueprint("company", __name__, url_prefix="/company")


# This route will return a list of all companies in the database
@company_router.route("/list", methods=["GET"])
def list_companies():
    companies = Company.query.all()
    json_companies = list(map(lambda company: company.to_json(), companies))
    return jsonify({"companies": json_companies})


# This route will create a new company in the database
@company_router.route("/create", methods=["POST"])
def create_company():
    name = request.json.get("name")
    address = request.json.get("address")
    city = request.json.get("city")
    state = request.json.get("state")
    zip = request.json.get("zip")
    owner_id = request.json.get("ownerId")

    if not name or not address or not city or not state or not zip or not owner_id:
        return jsonify({"error": "Missing required fields"}), 400

    owner = User.query.get(owner_id)
    if not owner:
        return jsonify({"error": "Owner not found"}), 404

    new_company = Company(
        name=name,
        address=address,
        city=city,
        state=state,
        zip=zip,
        owner_id=owner_id
    )

    try:
        db.session.add(new_company)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"company": new_company.to_json()}), 201


# This route will update a company in the database
@company_router.route("/update/<int:company_id>", methods=["PATCH"])
def update_company(company_id):
    company = Company.query.get(company_id)

    if not company:
        return jsonify({"error": "Company not found"}), 404

    data = request.json
    company.name = data.get("name", company.name)
    company.address = data.get("address", company.address)
    company.city = data.get("city", company.city)
    company.state = data.get("state", company.state)
    company.zip = data.get("zip", company.zip)
    company.owner_id = data.get("ownerId", company.owner_id)

    try:
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"company": company.to_json()}), 200


# This route will delete a company from the database
@company_router.route("/delete/<int:company_id>", methods=["DELETE"])
def delete_company(company_id):
    company = Company.query.get(company_id)

    if not company:
        return jsonify({"error": "Company not found"}), 404

    try:
        db.session.delete(company)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"message": "Company deleted"}), 200