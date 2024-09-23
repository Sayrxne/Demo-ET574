#Lab3_1.py
#Chasyl De Guzman


#variable
bill = float(input("Enter the amount of bill: "))
tipPercent = int(input("Enter the percentage of the tip: "))
tip = float((bill*tipPercent)/100)

#print
print("Tip: $",round(tip, 2))
