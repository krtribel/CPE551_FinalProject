# Swap

# embedded list
Posts = [['NJ', '1b', '1br', '$500', 'yes', 'yes'], ['NJ', '3b', '1br', '$700', 'no', 'yes'], ['NY', '2b', '2br', '$600', 'yes', 'yes'], ['NY', '3b', '2br', '$1000', 'no', 'no'], ['PA', '2b', '1br', '$300', 'no', 'yes'], [
    'PA', '2b', '2br', '$500', 'no', 'no'], ['DE', '4b', '2br', '$1100', 'yes', 'yes'], ['DE', '1b', '1br', '$200', 'no', 'no'], ['MA', '2b', '2br', '$700', 'yes', 'yes'], ['MA', '2b', '2br', '$650', 'no', 'yes']]

# login with my_django_app

# start program

print("Welcome to the Swap Apartment Finder! Please answer the following questions so we can match you with a place to stay! (Please type responses exactly how shown in Options)")

state = input(
    "What state are you looking for? (Options are NJ, NY, PA, DE, MA):")
print("State: " + state)

bedrooms = input("How many bedrooms are you looking for? (Options are 1-4):")
print("Bedrooms: " + bedrooms)

bathrooms = input("How many bathrooms are you looking for? (Options are 1-2):")
print("Bathroom: " + bathrooms)

price = input("What is you max price? (Do not enter $):")
print("Price: " + price)

pets = input("Pets? (Options are yes or no):")
print("Pets: " + pets)

utilities = input("Utilities included? (Options are yes or no):")
print("Utilities: " + utilities)


newL = []

for i in Posts:
    if i[0] == state:
        newL.append(i)

newL2 = []

for i in newL:
    if i[1] >= bedrooms:
        newL2.append(i)

newL3 = []

for i in Posts:
    if i[2] >= bathrooms:
        newL3.append(i)

newL4 = []

for i in newL:
    if i[3] <= price:
        newL4.append(i)

newL5 = []

for i in Posts:
    if i[4] == pets:
        newL5.append(i)

newL6 = []

for i in newL:
    if i[5] == utilities:
        newL6.append(i)

if newL6:
    print("Here are the available listings that match you criteria: ")
    print(newL6)

else:
    print("Oops! There are no available apartments fitting your criteria.")
