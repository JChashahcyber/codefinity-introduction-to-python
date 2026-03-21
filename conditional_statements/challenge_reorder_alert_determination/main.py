stock_count = 8
reorder_threshold = 10
has_pending_order = False
is_seasonal_item = False
reorder_alert = stock_count < reorder_threshold and not has_pending_order or is_seasonal_item 