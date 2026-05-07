from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Server Running"

@app.route("/ai", methods=["POST"])
def ai():

    data = request.json
    text = data.get("text", "")

    # TEMP AI LOGIC (we will upgrade to Claude later)
    if "happy" in text:
        emotion = "happy"
    elif "sad" in text:
        emotion = "sad"
    elif "think" in text:
        emotion = "thinking"
    else:
        emotion = "idle"

    return jsonify({
        "reply": "I heard you say: " + text,
        "emotion": emotion
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
