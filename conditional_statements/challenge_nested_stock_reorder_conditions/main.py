current_stock = 15
reorder_level = 20
supplier_lead_time = 5
order_action = ""

if current_stock < reorder_level:
    if supplier_lead_time > 3:
        order_action = "expedite"
    else:
        order_action = "standard"
else:
    order_action = "none"

print(order_action)