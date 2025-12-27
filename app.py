from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# 1. Backend for Disease Detection
@app.route('/detect', methods=['POST'])
def detect_disease():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    # In a real project, you would load your .h5 or .pth model here
    # For now, we simulate a result:
    return jsonify({"result": "Leaf Spot detected (Example Result)"})

# 2. Backend for Crop Recommendation
@app.route('/recommend', methods=['POST'])
def recommend_crop():
    data = request.json
    # Logic: Read N, P, K, and pH from 'data'
    # Example: model.predict([[data['n'], data['p'], data['k'], data['ph']]])
    return jsonify({"result": "Based on soil data, Wheat is recommended."})

# 3. Backend for Chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')
    # Simple logic or integration with OpenAI/Gemini API
    return jsonify({"answer": f"You asked about '{user_msg}'. Here is the farming advice..."})

if __name__ == '__main__':
    app.run(debug=True)
