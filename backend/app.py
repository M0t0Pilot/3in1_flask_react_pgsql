from flask import Flask, request, jsonify
import paypalrestsdk

app = Flask(__name__)

# Настройка PayPal SDK
paypalrestsdk.configure({
    "mode": "sandbox",  # sandbox или live
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET"
})

@app.route('/payment', methods=['POST'])
def create_payment():
    data = request.json
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": "http://localhost:5000/payment/execute",
            "cancel_url": "http://localhost:5000/"
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Item",
                    "sku": "item",
                    "price": "10.00",
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": "10.00",
                "currency": "USD"
            },
            "description": "This is the payment description."
        }]
    })

    if payment.create():
        return jsonify({'id': payment.id})
    else:
        return jsonify({'error': payment.error}), 400

if __name__ == '__main__':
    app.run(debug=True)
