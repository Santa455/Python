# Collection of numbers
positive = []
negative = []
value = float(input("Please enter a positive or negative number (enter a zero to end): "))
# Loop while keepGoing is true
while value != 0:
# If positive, add to positive collection
    if value > 0:
        positive.append(value)
# If negative, add to negative collection
    elif value < 0:
        negative.append(value)
# Read in value from user
value = float(input("Please enter a positive or negative number (enter a zero to end): "))
# Output two collections
print("Positive Values Entered: " + str(positive))
print("Negative Values Entered: " + str(negative))