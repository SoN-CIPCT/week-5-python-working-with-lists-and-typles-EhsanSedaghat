#List
#Create a list that contains 6 items.
blood_pressure_medications = ["Lisinopril","Amlodipine","Losartan","Hydrochlorothiazide","Metoprolol","Valsartan"]

#Print the items in the list to the output console.
print(blood_pressure_medications)

#Print the first two items in the list using a slice.
print(blood_pressure_medications[0:2])

#Print the middle two items in the list using a slice.
print(blood_pressure_medications[2:4])

#Print the first and last items in the list using indexes.
print({blood_pressure_medications[0],blood_pressure_medications[-1]})

#Tuple
#A restaurant only offers five basic foods on its menu. Decide on these five foods and store them in a tuple.
sandwiches = ("steak","chicken","veggies","cheese","combo")

#Print each item on the menu using a for loop.
for item in sandwiches:
    print("I like " + item)
    print("sounds great!")

print("ENJOY!")

#The restaurant has updated its menu, replacing two of the items with different foods. Copy the tuple replacing two of the foods on the menu.
sandwich_list = list(sandwiches)
sandwich_list[2] = "tuna"
sandwich_list[4] = "turkey"

updated_sandwiches = tuple(sandwich_list)

print(updated_sandwiches)

#Print each item on the revised menu using a loop.

for item in updated_sandwiches:
    print("I like " + item)
    print("sounds great!")

print("ENJOY!")
