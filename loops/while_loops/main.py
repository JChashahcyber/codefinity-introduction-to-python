start_number = 5
countdown_values = []
while start_number >= 1:
    print(f"Current start number: {start_number}")
    countdown_values.append(start_number)
    start_number -=1
print("Discount countdown complete!")
print(countdown_values)