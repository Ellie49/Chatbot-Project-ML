from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_model import ChatbotModel

app = Flask(__name__)
# Allow requests from any origin (so you can open index.html directly)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load the chatbot once at startup
bot = ChatbotModel(kb_path="knowledge_base.json")

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "Chatbot backend running"}), 200

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_message = (data.get("message") or "").strip()
    reply = bot.get_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    # Run on 127.0.0.1:5000
    app.run(host="127.0.0.1", port=5000, debug=True)