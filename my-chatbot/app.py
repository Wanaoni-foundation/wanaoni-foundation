from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    response = {"text": "Hello, world!"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

