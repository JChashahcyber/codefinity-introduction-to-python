current_stock = 8
reorder_level = 10
needs_reorder = None  # assign True or False based on stock comparison

if current_stock < reorder_level:
    needs_reorder = True
else:
    needs_reorder = False

print(needs_reorder)