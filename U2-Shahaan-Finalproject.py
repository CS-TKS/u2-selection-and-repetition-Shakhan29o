print("Welcom to the Food waste Logger!")
print("Track how much food you waste each day for a week")

#List to store food waste amount
food_waste = []

#Loop for 7 days(a week)
for day in range (1, 8):
    waste = float(input(f"Day {day}: enter food waste in grams:"))
    food_waste.append(waste)

#calculations fo total and average
total = sum(food_waste)                 # total food waste
average = total/7                       #divided by 7 because its a week

#output results ( not final)
print(f"--- Weekly Summary ---")
print(f"Total food waste: {total} grams")
print(f"Average waste daily: {average:.1} grams")