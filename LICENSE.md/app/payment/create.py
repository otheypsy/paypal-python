import paypalrestsdk
from helpers.Items import Item
from helpers.Redirect import Redirect
from helpers.Transaction import Transaction
import pprint


currency = 'USD'
redirect_object = Redirect()
redirect_object.set_return_url('http://localhost:3000/payment/execute')
redirect_object.set_cancel_url('http://localhost:3000/')

item_array = list()
for i in range(4):
    item = Item(currency)
    item.name = 'name ' + str(i)
    item.sku = i
    item.price += i
    item_array.append(item)

transaction_object = Transaction(currency)
transaction_object.item_list(item_array)

test = {
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": redirect_object.create_array(),
    "transactions": [transaction_object.create_array()]
}

payment = paypalrestsdk.Payment(test)
pprint.pprint(test)

if payment.create():
    print("Payment created successfully")
    for link in payment.links:
        if link.rel == "approval_url":
            # Convert to str to avoid Google App Engine Unicode issue
            # https://github.com/paypal/rest-api-sdk-python/pull/58
            approval_url = str(link.href)
            print("Redirect for approval: %s" % (approval_url))
else:
    print(payment.error)

