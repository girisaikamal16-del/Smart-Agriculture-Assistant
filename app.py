from flask import Flask, request, jsonify
import pickle

app = Flask(__AGRI__)

crop_model = pickle.load(open("crop_model.pkl", "rb"))

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    prediction = crop_model.predict([[data["N"], data["P"], data["K"], data["pH"]]])
    return jsonify({"crop": prediction[0]})

@app.route("/")
def home():
    return "Smart Agriculture AI Backend Running"

if __AGRI__ == "__main__":
    app.run(debug=True)
