print("Welcome to the Food waste Logger!")
print("Track how much food you waste each day for a week")

#List to store food waste amount
food_waste = []

#Loop for 7 days(a week)
for day in range (1, 8):
    print("Day {day}:")
    food_name = input("What food did you waste today(or 'none' if non was wasted): ") #Addition feature that also asks type of food wasted
    #Adding the none feature so that the client has a choice to say he wasted no food that day
    if food_name.lower(0) == "none":
        food_waste.append(0)
        print("Good job! you wasted no food today!")
     #ask for waste input
    else:
     waste = float(input(f"Day {day}: enter food waste in grams:"))
     # add whatever waste amount to list
    food_waste.append(waste)

#calculations fo total Waste.append(waste)nd average
total = sum(food_waste)                 # total food waste
average = total/7                       #divided by 7 because its a week

#show weekly results
print(f"--- Weekly Summary ---")
print(f"Total food waste: {total} grams")
print(f"Average waste daily: {round (average, 2)} grams")

#give feedabck based on how much food wasted on average
if average<50:
    print("Amazing job! your wasting very less food, Keep this up!")
elif average<100:
    print("Good job, But theres still room to improve!")
else:
    print("Try reducing food waste next week!")

#end of program
print("\nThank you for using The Food Waste Logger! Come back next week!")