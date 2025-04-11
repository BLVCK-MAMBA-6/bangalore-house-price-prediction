from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import util

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Route to get location names (GET request only)
@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    return response

# Route to predict home price (POST request only)
@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Check if JSON is sent in the request
        if request.is_json:
            data = request.get_json()
            total_sqft = float(data['total_sqft'])
            location = data['location']
            bhk = int(data['bhk'])
            bath = int(data['bath'])
        else:
            # For form data
            total_sqft = float(request.form['total_sqft'])
            location = request.form['location']
            bhk = int(request.form['bhk'])
            bath = int(request.form['bath'])

        # Get the estimated price
        response = jsonify({
            "estimated_price": util.get_estimated_price(location, total_sqft, bhk, bath)
        })
        return response

    except Exception as e:
        # Handle any exception, for example, missing form data
        return jsonify({"error": f"An error occurred: {str(e)}"}), 400


if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()  # Ensure saved artifacts are loaded before the server starts
    app.run(debug=True, port=8080)  # Set to debug mode for more informative error messages
