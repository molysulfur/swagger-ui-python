from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint

REQUEST_API = Blueprint('request_api', __name__)

PARTNER_RESPONSE = [ {
        'accountNumber': 1234,
        'id': 1,
        'date_joined': (datetime.today() - timedelta(1)).timestamp(),
        'email': u'testuser2@test.com',
        'first_name':'Dream',
        'last_name':'CUP-E',
        'state' : '',
        'telephone' : '191',
        'total_commission' : 0,
        'total_deposit':0,
        'total_withdrawal':0
    },
    {
        'accountNumber': 5678,
        'id': 2,
        'date_joined': (datetime.today() - timedelta(1)).timestamp(),
        'email': u'testuser2@test.com',
        'first_name':'Dream',
        'last_name':'CUP-E',
        'state' : '',
        'telephone' : '191',
        'total_commission' : 0,
        'total_deposit':0,
        'total_withdrawal':0
    }
]

def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

@REQUEST_API.route('/partners', methods=['GET'])
def getPartners():
    """Return all book requests
    @return: 200: an array of all known PARTNER_RESPONSE as a \
    flask/response object with application/json mimetype.
    """
    return jsonify(PARTNER_RESPONSE)


@REQUEST_API.route('/partner/<string:accountNumber>', methods=['GET'])
def getPartner(accountNumber):
    """Return all book requests
    @return: 200: an array of all known PARTNER_RESPONSE as a \
    flask/response object with application/json mimetype.
    """
    for account in PARTNER_RESPONSE:
        if account['accountNumber'] == int(accountNumber):
            return jsonify(account)
    
    return jsonify(error=400,text="bad request") , 400
    

