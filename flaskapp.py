from flask import Flask, jsonify, request, send_from_directory, redirect, url_for
from utils import constants as c
from restapphelpers.similartyrequest import SimilarityRequest
from aggregators.aggregators_factory import AggregatorFactory
import json
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app)


@app.route('/visualisation/<path:filename>')
def get_visualisation(filename):
    return send_from_directory(filename)


@app.route('/', methods=['GET'])
def get_home_page():
    return redirect('/visualization/minkowski.html')


@app.route('/fuzzy/similarity/methods', methods=['GET'])
def get_implemented_similarity_calculation_methods():
    return jsonify({
        'methods': c.IMPLEMENTED_METHODS,
        'status': "OK"
    })


aggregatorFactory = AggregatorFactory()


@app.route('/fuzzy/aggregators', methods=['GET'])
def get_implemented_aggregators():
    return jsonify({
        'values': aggregatorFactory.getSupportedAggregators(),
        'status': "OK"
    })


@app.route('/fuzzy/similarity', methods=['POST'])
def calculate_zsimilarity():
    requestBody = request.get_json(force=True)
    print "Got request with body: " + str(requestBody)
    try:
        parsedRequest = SimilarityRequest(requestBody)
        result = parsedRequest.calculate()
        return jsonify({
            c.METHOD_REQUEST_PARAMETER_NAME: parsedRequest.method,
            c.CONFIG_REQUEST_PARAMETER_NAME: str(parsedRequest.rawConfig),
            c.RESULT_REQUEST_PARAMETER_NAME: result,
            c.SET_A_REQUEST_PARAMETER_NAME: parsedRequest.setA,
            c.SET_B_REQUEST_PARAMETER_NAME: parsedRequest.setB,
            'status': "OK"
        })
    except Exception as e:
        print e
        responseBody = {
            'status': "FAILURE",
            'message': str(e)
        }
        return jsonify(responseBody), 400


def get_request_map(request):
    data = request.data
    return json.loads(data)


if __name__ == '__main__':
    app.run(debug=True)
