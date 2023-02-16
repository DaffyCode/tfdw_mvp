from flask import Flask, jsonify, request, Blueprint
from datetime import datetime
from models.donation_request import DonationRequest, donation_request_schema, donation_requests_schema
from models.user import User
from extensions import db

from api.user import token_required

donation_request_route = Blueprint('donation_request_route', __name__)


@donation_request_route.route('/api/donation_request', methods=['POST'])
@token_required
def create_donation_request(current_user):
    """
    Creates a new donation request entity in the donation_requests database table.
    Returns: json with donation request data
    """
    user_id = current_user.id
    date = datetime.now()
    category = request.json.get('category', '')
    amount = request.json.get('amount', '')
    size_1 = request.json.get('size_1', '')
    size_2 = request.json.get('size_2', '')
    color_1 = request.json.get('color_1', '')
    description = request.json.get('description', '')
    status = "offen"

    donation_request = DonationRequest(user_id=user_id,
                                       date=date,
                                       category=category,
                                       amount=amount,
                                       size_1=size_1,
                                       size_2=size_2,
                                       color_1=color_1,
                                       description=description,
                                       status=status)

    db.session.add(donation_request)
    db.session.commit()

    return donation_request_schema.jsonify(donation_request)


@donation_request_route.route('/api/donation_request', methods=['GET'])
@token_required
def get_donation_requests(current_user):
    """
    Get all donation requests from the database table donation_requests.
    Returns: json with list of all donation requests
    """
    # all_donation_requests = DonationRequest.query.all()
    # return jsonify(donation_requests_schema.dump(all_donation_requests))
    results = (db.session.query(DonationRequest.id, DonationRequest.date, DonationRequest.category,
                                DonationRequest.amount, DonationRequest.size_1, DonationRequest.size_2,
                                DonationRequest.color_1, DonationRequest.description, User.first_name, User.last_name,
                                User.email, User.zip_code, User.city)
               .join(User, User.id == DonationRequest.user_id)).all()

    return jsonify([dict(id=x.id, date=x.date, category=x.category, amount=x.amount, size_1=x.size_1, size_2=x.size_2,
                         color_1=x.color_1, description=x.description, first_name=x.first_name,
                         last_name=x.last_name, email=x.email, zip_code=x.zip_code, city=x.city) for x in results])


@donation_request_route.route('/api/donation_request/<int:donation_request_id>', methods=['GET'])
@token_required
def get_donation_request(current_user, donation_request_id: int):
    """
    Gets a specific donation request by id from the donation_requests database table.
    Args:
        donation_request_id: id of donation request
    Returns: json with donation request data
    """
    donation_request = DonationRequest.query.get(donation_request_id)
    return donation_request_schema.jsonify(donation_request)


@donation_request_route.route('/api/donation_request/<int:donation_request_id>', methods=['PATCH'])
@token_required
def update_donation_request(current_user, donation_request_id: int):
    """
    Updates a given donation request by id in the donation requests database table.
    Args:
        donation_request_id: id of donation request to be updated
    Returns: json of updated donation request
    """
    user_id = current_user.id
    date = datetime.now()
    category = request.json.get('category', '')
    amount = request.json.get('amount', '')
    size_1 = request.json.get('size_1', '')
    size_2 = request.json.get('size_2', '')
    color_1 = request.json.get('color_1', '')
    description = request.json.get('description', '')
    status = request.json.get('status', '')

    donation_request = DonationRequest.query.get(donation_request_id)
    donation_request.user_id = user_id
    donation_request.date = date
    donation_request.category = category
    donation_request.amount = amount
    donation_request.size_1 = size_1
    donation_request.size_2 = size_2
    donation_request.color_1 = color_1
    donation_request.description = description
    donation_request.status = status

    db.session.add(donation_request)
    db.session.commit()

    return donation_request_schema.jsonify(donation_request)


@donation_request_route.route("/api/donation_request/<int:donation_request_id>", methods=['DELETE'])
@token_required
def delete_donation(current_user, donation_request_id: int):
    """
    Deletes a donation request by id from the donation_requests database table.
    Args:
        donation_request_id: id of donation request to be deleted
    Returns: json of deleted donation request entity from database table donation requests
    """
    donation_request = DonationRequest.query.get(donation_request_id)
    db.session.delete(donation_request)
    db.session.commit()
    return donation_request_schema.jsonify(donation_request)
