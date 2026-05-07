from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ai", methods=["POST"])
def ai():

    data = request.get_json(force=True)
    text = data.get("text", "")

    return jsonify({
        "reply": f"You said: {text}",
        "emotion": "happy"
    })

@app.route("/")
def home():
    return "AI SERVER ONLINE"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
