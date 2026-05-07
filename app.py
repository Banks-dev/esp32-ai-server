from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# ================== CLAUDE CONFIG ==================
CLAUDE_API_KEY = "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"

CLAUDE_URL = "https://api.anthropic.com/v1/messages"

HEADERS = {
    "x-api-key": CLAUDE_API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
}

# ================== EMOTION ENGINE ==================
def detect_emotion(text):
    text = text.lower()

    if any(w in text for w in ["happy", "great", "awesome", "good"]):
        return "happy"

    if any(w in text for w in ["sad", "sorry", "bad", "upset"]):
        return "sad"

    if any(w in text for w in ["think", "hmm", "maybe", "analyze"]):
        return "thinking"

    if any(w in text for w in ["fire", "🔥", "hype", "drop"]):
        return "hype"

    return "idle"


# ================== MAIN AI ROUTE ==================
@app.route("/ai", methods=["POST"])
def ai():

    data = request.json
    user_text = data.get("text", "")

    try:
        payload = {
            "model": "claude-3-5-sonnet-latest",
            "max_tokens": 300,
            "messages": [
                {
                    "role": "user",
                    "content": user_text
                }
            ]
        }

        r = requests.post(CLAUDE_URL, headers=HEADERS, json=payload)
        result = r.json()

        reply = result["content"][0]["text"]

        return jsonify({
            "reply": reply,
            "emotion": detect_emotion(reply)
        })

    except Exception as e:
        return jsonify({
            "reply": "AI server error",
            "emotion": "error"
        })


# ================== RUN SERVER ==================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)