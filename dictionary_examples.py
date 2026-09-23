# Creating a dictionary
person = {
    "name": "X0de",
    "age": "13",
    "location": "Earth"
}

print(person)

# Accessing values
print(person["name"])
print(person["age"])

# Adding data
person["hobby"] = "coding"
print(person)

# Changing data
person["age"] = 14
print(person)

# Removing data
person.pop("location")
print(person)

# Looping through dictionary
for key in person:
    print(key, person[key])
