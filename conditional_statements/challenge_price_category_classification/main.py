item_price = 25
price_category = None

if item_price < 20:
    price_category = "budget"
elif item_price <= 50:
    price_category = "standard"
else:
    price_category = "premium"
print(price_category)