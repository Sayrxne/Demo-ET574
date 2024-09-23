#Lab3_3.py
#Chasyl De Guzman

#variable
a = int(input("Please enter the first integer: "))
b = int(input("Please enter the second integer: "))
c = int(input("Please enter the third integer: "))
x = [a,b,c]

#using max(),min(), and remove to remove the max and min for // 
#variable mid to only print the center interger

Min = min(x)
x.remove(min(x))
Max = max(x)
x.remove(max(x))
Mid = x[0]

#print
print("Before sorting:", a,b,c)
print("After sorting:", Min, Mid, Max)
