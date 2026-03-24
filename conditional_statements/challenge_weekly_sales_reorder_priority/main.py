weekly_sales = 120
current_stock = 30
reorder_priority = "high" if weekly_sales > 100 and current_stock <50 else "normal"