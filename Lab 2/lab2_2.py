#Lab2_2.py
#Chasyl De Guzman

#Variable
email = "BurgerByTheBay@Food.restaraunt.com"

#print 
x = email.find("@")
print("Email Address: " + email)
print("User name: " + email[:x].lower())

y = email.rfind(".com")
print("Company name:" + email[x+1:y].upper())
