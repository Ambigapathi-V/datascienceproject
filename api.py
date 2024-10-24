from flask import Flask, request, jsonify
import numpy as np
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])  # API route for prediction
def predict_api():
    try:
        # Extracting JSON data from the request
        data = request.json
        features = np.array([[data['fixed_acidity'], data['volatile_acidity'], data['citric_acid'],
                              data['residual_sugar'], data['chlorides'], data['free_sulfur_dioxide'],
                              data['total_sulfur_dioxide'], data['density'], data['pH'],
                              data['sulphates'], data['alcohol']]])

        # Predicting using the model pipeline
        obj = PredictionPipeline()
        prediction = obj.predict(features)

        return jsonify({'prediction': str(prediction[0])})  # Return prediction as JSON
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)  # API runs on a different port
