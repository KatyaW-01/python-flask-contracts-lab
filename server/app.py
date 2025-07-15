#!/usr/bin/env python3
import os
from flask import Flask, g, make_response

app = Flask(__name__)

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/contract/<int:id>')
def contractor_info(id):
    for contract in contracts:
        if id == contract['id']:
            response_body = contract.get('contract_information')
            status_code = 200
            headers = {}
            return make_response(response_body, status_code, headers)
    
    response_body = 'Contract not found'
    status_code = 404
    headers = {}
    return make_response(response_body, status_code, headers)    

@app.route('/customer/<string:customer_name>')
def customer_info(customer_name):
    if customer_name in customers:
        response_body = ""
        status_code = 204
        headers = {}
        return make_response(response_body, status_code, headers)
    
    response_body = "Customer not found"
    status_code = 404
    headers = {}
    return make_response(response_body, status_code, headers)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
