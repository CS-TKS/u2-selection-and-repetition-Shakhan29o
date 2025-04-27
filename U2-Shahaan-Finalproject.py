Print("Welcom to the Food waste Logger!")
Print("Track how much food you waste each day for a week")

#List to store food waste amount
food_waste = []

#Loop for 7 days(a week)
for day in range (1, 8):
    waste = float(input(f"Day [day]: enter food waste in grams:")