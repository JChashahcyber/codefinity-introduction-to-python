product_price = 100.0
stock_quantity = 20
discountRate = 0.1
discountedPrice = product_price * (1 -discountRate)
inventoryValue = discountedPrice * stock_quantity
print (inventoryValue)