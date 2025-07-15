#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<id>')
def contractor_info():
    pass

@app.route('/customer/<customer_name>')
def customer_info():
    pass


if __name__ == '__main__':
    app.run(port=5555, debug=True)
