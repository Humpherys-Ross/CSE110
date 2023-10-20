# Allow for the user to search via year or country

# Download the dataset and write a Python program to analyze it to answer the
# following questions:

# What is the year and country that has the lowest life expectancy in the
# dataset?

# What is the year and country that has the highest life expectancy in the
# dataset?

# Allow the user to type in a year, then, find the average life expectancy for
# that year. Then find the country with the minimum and the one with the
# maximum life expectancies for that year.

# A sample run could look as follows:

# ### Life expectancy data analysis ###
# Enter the year of interest: 1959

# The overall max life expectancy is: 86.751 from Monaco in 2019
# The overall min life expectancy is: 17.76 from Iceland in 1882

# For the year 1959:
# The average life expectancy across all countries was 54.95
# The max life expectancy was in Norway with 73.49
# The min life expectancy was in Mali with 28.077
#####################################

# Milestone Requirements:

# By the middle of the week, to help make sure you are on track to finish the
# assignment, you need to complete the following:

# 1 Download the dataset
# 2 Load the dataset in your Python program
# 3 Iterate through the data line by line
# 4 Split each line into parts
# 5 Find the lowest value for life expectancy and the highest value for life
#   expectancy in the dataset, and display both values. (Note that at this
#   point, you just need the value for this, not the year and the country for
#   that value.)

# #####################################

# initialize variables to store max and min life expectancy
# use infinity as the initial value
min_life_expectancy = float("inf")
min_life_country = ""
min_life_year = ""

# use negative infinity as the initial value
max_life_expectancy = float("-inf")
max_life_country = ""
max_life_year = ""

# create a dictionary to store the average life expectancy for each year
life_expectancies_by_year = {}

# create a dictionary to store the average life expectancy for each country
life_expectancies_by_country = {}

# open the file, week6/life-expectancy.csv and read it line by line
with open("Week6/life-expectancy.csv", "r") as file:
    # skip the first line
    next(file)

    for line in file:
        # split the line into parts stripping the newline character
        # and splitting on the comma
        parts = line.strip().split(",")

        # get the year, country, and life expectancy from the parts
        entity, code, year, life_expectancy = parts
        year = int(year)
        life_expectancy = float(life_expectancy)

        # check if the current life expectancy is the new min
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_life_country = entity
            min_life_year = year

        # check if the current life expectancy is the new max
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_life_country = entity
            max_life_year = year

        # check if the year is already in the dictionary
        if year not in life_expectancies_by_year:
            life_expectancies_by_year[year] = []

        # add the life expectancy to the list for the year
        life_expectancies_by_year[year].append((entity, life_expectancy))

        # check if the country is already in the dictionary
        if entity not in life_expectancies_by_country:
            life_expectancies_by_country[entity] = []

        # add the life expectancy to the list for the country
        life_expectancies_by_country[entity].append((year, life_expectancy))

# ask the user whether they want to search by year or country
search_type = input("Do you want to search by (Y)ear or (C)ountry? ")
search_type = search_type.strip().lower()  # This is for formatting purposes

if search_type == "y":

    # ask the user for a year
    user_year = int(input("Enter the year of interest: "))

    # calculate the average life expectancy for the year
    if user_year in life_expectancies_by_year:
        life_expectancies = [le for _, le in
                             life_expectancies_by_year[user_year]]
        avg_life_expectancy = sum(life_expectancies) / len(life_expectancies)
    else:
        avg_life_expectancy = None

    # find the max and min life expectancies for the year
    min_life_country_user = ""
    min_life_expectancy_user = float("inf")

    max_life_country_user = ""
    max_life_expectancy_user = float("-inf")

    if user_year in life_expectancies_by_year:
        for entity, life_expectancy in life_expectancies_by_year[user_year]:
            if life_expectancy < min_life_expectancy_user:
                min_life_expectancy_user = life_expectancy
                min_life_country_user = entity

            if life_expectancy > max_life_expectancy_user:
                max_life_expectancy_user = life_expectancy
                max_life_country_user = entity

    # print the results
    print(f"The overall max life expectancy is: {max_life_expectancy} from"
          f" {max_life_country} in {max_life_year}")
    print(f"The overall min life expectancy is: {min_life_expectancy} from"
          f" {min_life_country} in {min_life_year}")

    # print the results for the user's year
    if avg_life_expectancy is not None:
        print(f"\nFor the year {user_year}:")
        print(f"The average life expectancy across all countries was"
              f" {avg_life_expectancy:.2f}")
        print(f"The max life expectancy was in {max_life_country_user} with"
              f" {max_life_expectancy_user}")
        print(f"The min life expectancy was in {min_life_country_user} with"
              f" {min_life_expectancy_user}")
    else:
        print(f"\nNo data for {user_year}")
elif search_type == 'c':
    # ask the user for a country
    user_country = input("Enter the country of interest: ").capitalize()

    if user_country in life_expectancies_by_country:
        # find the data for the country
        country_data = life_expectancies_by_country[user_country]

        # find the max and min life expectancies for the country
        # use the max and min functions with a lambda function
        max_year_country = max(country_data, key=lambda x: x[1])
        min_year_country = min(country_data, key=lambda x: x[1])

        # display the results for the user-specified country
        print(f"Country: {user_country}")
        print(f"The highest life expectancy was in {max_year_country[0]} in"
              f" {max_year_country[1]:.2f} years.")
        print(f"The lowest life expectancy was in {min_year_country[0]} in"
              f" {min_year_country[1]:.2f} years.")
    else:
        print(f"\nNo data for {user_country}")
else:
    print("Invalid choice. Please type "'Y'" for year or "'C'" for country.")
