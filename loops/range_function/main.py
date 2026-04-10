# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Loop over the list indices
for i in range(len(weekdays)):
    weekday = weekdays[i]            # current weekday
    promotion = daily_promotions[i]  # corresponding promotion
    print(f"{weekday}: Promotion on {promotion}")