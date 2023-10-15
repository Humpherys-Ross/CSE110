people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# initialize variables to find the youngest age and name
youngest_age = 9999
youngest_name = ""

for person_data in people:
    print(person_data)

# split the string into name and age
for person_data in people:
    name, age_str = person_data.split()
    age = int(age_str)
    print(f"Name: {name}, Age: {age}")

    # find the youngest age and name
    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f"Youngest person is {youngest_name} who is {youngest_age} years old.")
