initial_stock = 100
sold_units = 20
new_shipment = 50
cost_price = 5.0
selling_price = 8.0
updated_stock  = (initial_stock - sold_units + new_shipment)
revenue = (sold_units * selling_price)
profit = (sold_units * (selling_price -cost_price))
print(updated_stock)
print(revenue)
print(profit)