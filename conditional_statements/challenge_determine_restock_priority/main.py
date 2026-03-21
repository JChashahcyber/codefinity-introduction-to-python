stock_count = 5
min_stock = 10
is_organic = True
is_local = False
has_backorder = False
restock_priority = stock_count < min_stock and (is_organic or not is_local) and not has_backorder