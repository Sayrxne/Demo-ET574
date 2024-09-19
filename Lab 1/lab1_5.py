#Chasyl De Guzman
firstFill = 23456.0
secondFill = 23678.0
gallonUsed = 10.0
averageMiles = (firstFill+secondFill)/2
milesPerGallon = averageMiles/gallonUsed
Answer = round(milesPerGallon, 3)


print("Example Output")
print("Distance Traveled:",averageMiles,"Miles")
print("Gallons Used:",gallonUsed,"Gallons")
print("How many miles per gallon did the car average between two fillings?")
print("Answer:",Answer, "Miles/Gallon")