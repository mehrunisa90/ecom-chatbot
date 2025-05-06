from flask import Flask, request, jsonify

app = Flask(__name__)

orders = {
    "12345": "Your order #12345 has been shipped and will arrive in 2 days.",
    "45678": "Your order #45678 is being packed and will be shipped tomorrow.",
    "99999": "Your order #99999 has been delivered. We hope you loved it!"
}

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    
    parameters = req.get('queryResult', {}).get('parameters', {})
    order_number = str(parameters.get('number'))

    response_text = orders.get(order_number, f"Sorry, I couldn't find order #{order_number} in our system.")
    
    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)