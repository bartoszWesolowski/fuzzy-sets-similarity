from flask import Flask, jsonify
from flask import request
from utils import constants as c
from similartyRequest import SimilarityRequest
import json

from flask_cors import CORS
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

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
