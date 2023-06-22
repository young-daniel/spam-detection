import flask
import pickle
from flask import jsonify, request
from preprocessing import clean_message

with open('pipeline.pickle', 'rb') as f:
    pipeline = pickle.load(f)
output_map = {0:'ham', 1:'spam'}

app = flask.Flask('spam-detection')

# for sanity checks, nothing fancy
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
    text = clean_message(text)
    result = pipeline.predict([text])
    result = output_map[result[0]]
    return jsonify(result)


if __name__ == '__main__':
    app.run()