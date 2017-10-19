from datetime import date

name = "Anil Varre"
dob = date(1975,7,11)
languages = ["English","Telugu"]
favorites = {"movie":"Predator","food":"Chicken Biryani"}

address1 = "48224 Heather Ct"
city = "Northville"
state = "MI"
country = "USA"

print("Street : %s" % address1)
print("City : %s" % city)
print("State : %s" % state)
print("Country : %s " % country)
print("\n"*1)
for i in languages :
    print(i)

print("\n"*1)
languages.append("Tamil")

languages.insert(1,"Hindi")

for i in languages :
    print(i)

print("\n"*1)

for i in favorites.keys() :
    print("%s : %s" % (i, favorites.get(i)))


def calculateAge(db) :
    today = date.today()
    daysFromBirth = abs(today - db).days
    age = daysFromBirth//364.25
    return age

print("\n"*1)

print(calculateAge(dob))

