from flask import Flask, jsonify
from flask import request
from utils import constants as c
from similartyRequest import SimilarityRequest
import json

app = Flask(__name__)


@app.route('/fuzzy/similarity/methods', methods=['GET'])
def get_implemented_similarity_calculation_methods():
    return jsonify({
        'methods': c.IMPLEMENTED_METHODS,
        'status': "OK"
    })


@app.route('/fuzzy/similarity', methods=['POST', 'GET'])
def calculate_similarity():
    parsedRequest = SimilarityRequest(request.get_json(force=True))
    result = parsedRequest.calculate()
    return jsonify({
        'method': parsedRequest.method,
        'config': parsedRequest.config,
        'result': result,
        'status': "OK"
    })


def get_request_map(request):
    data = request.data
    return json.loads(data)


if __name__ == '__main__':
    app.run(debug=True)
