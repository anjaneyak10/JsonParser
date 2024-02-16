from app import app
from flask import request

from app.Service.jsonArrayParser import jsonArrayParser
from app.Service.parsingService import jsonParser

@app.route('/parseJson', methods = ['POST'])
def jsonParse():
    if request.data:
        return jsonParser(request.data.decode('utf-8'))
    else:
        return "No data received"


@app.route('/parseJsonArray', methods = ['POST'])
def jsonArrayParse():
    if request.data:
        return jsonArrayParser(request.data.decode('utf-8'))
    else:
        return "No data received"
