import flask
from flask import jsonify, request

app = flask.Flask('spam-detection')

@app.route('/api/v1/status', methods=['GET'])
def status():
    return jsonify('API running')

@app.route('/api/v1/predict', methods=['POST'])
def predict():
    text = request.form.get('message')
    if not text:
        return "Error: no message specified, please specify a message for classification"
    else:
        print("Received message: {}".format(text))
    # dummy result for now
    # need to add vectorization + model predict
    results = 'ham'
    print(results)
    return jsonify(results)


if __name__ == '__main__':
    app.run()