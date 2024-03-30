from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('./model/iris_model.pkl')

@app.route('/', methods=['GET'])
def home():
    return "Model Trained Successfully and Connected With Flask!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify(prediction=int(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)