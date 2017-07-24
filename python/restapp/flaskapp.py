from flask import Flask, jsonify, request
from utils import constants as c
from similartyRequest import SimilarityRequest
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/fuzzy/similarity/methods', methods=['GET'])
def get_implemented_similarity_calculation_methods():
    return jsonify({
        'methods': c.IMPLEMENTED_METHODS,
        'status': "OK"
    })


@app.route('/fuzzy/similarity', methods=['POST'])
def calculate_similarity():
    print "Got request with body: " + str(request.get_json(force=True))
    parsedRequest = SimilarityRequest(request.get_json(force=True))
    result = parsedRequest.calculate()
    return jsonify({
        c.METHOD_REQUEST_PARAMETER_NAME: parsedRequest.method,
        c.CONFIG_REQUEST_PARAMETER_NAME: str(parsedRequest.config),
        c.RESULT_REQUEST_PARAMETER_NAME: result,
        c.SET_A_REQUEST_PARAMETER_NAME: parsedRequest.setA,
        c.SET_B_REQUEST_PARAMETER_NAME: parsedRequest.setB,
        'status': "OK"
    })


def get_request_map(request):
    data = request.data
    return json.loads(data)


if __name__ == '__main__':
    app.run(debug=True)
