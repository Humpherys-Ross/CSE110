# Allow for the user to search via year or country
# I also refactored the code to use functions instead of just one big block of
# code. This makes it easier to read and understand what is going on.

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


# function to load the data from the provided file
def load_data(filename):
    # create a dictionary to store the average life expectancy for each year
    life_expectancies_by_year = {}
    life_expectancies_by_country = {}

    # initialize variables to store max and min life expectancy
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    min_life_country = ''
    max_life_country = ''
    min_life_year = 0
    max_life_year = 0

    # open the file
    with open(filename, 'r') as file:
        # skip the first line
        next(file)

        # iterate through the data line by line
        for line in file:
            # strip the newline character and split the line into parts
            parts = line.strip().split(',')
            # unpack the parts into variables
            entity, code, year, life_expectancy = parts
            # convert year and life_expectancy to the appropriate data types
            year = int(year)
            life_expectancy = float(life_expectancy)

            # find the lowest value for life expectancy and the highest value
            # for life expectancy in the dataset
            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                min_life_country = entity
                min_life_year = year

            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                max_life_country = entity
                max_life_year = year

            # store the average life expectancy for each year
            if year not in life_expectancies_by_year:
                life_expectancies_by_year[year] = []

            life_expectancies_by_year[year].append((entity, life_expectancy))

            # store the average life expectancy for each country
            if entity not in life_expectancies_by_country:
                life_expectancies_by_country[entity] = []

            life_expectancies_by_country[entity].append((year,
                                                         life_expectancy))

    # return the life_expectancies_by_year and life_expectancies_by_country
    # dictionaries and the min and max life expectancies and their
    # corresponding countries and years
    return (
        life_expectancies_by_year,
        life_expectancies_by_country,
        min_life_expectancy,
        min_life_country,
        min_life_year,
        max_life_expectancy,
        max_life_country,
        max_life_year
    )


# function to get the data for a year
def get_year_data(year, data_by_year):
    # check if the year is in the dictionary
    if year not in data_by_year:
        # if not, return None
        return None

    # get the life expectancies for the year
    life_expectancies = [le for _, le in data_by_year[year]]
    avg_life_expectancy = sum(life_expectancies) / len(life_expectancies)

    # set the min and max life expectancies variables
    min_life_country_user = ""
    min_life_expectancy_user = float("inf")

    max_life_country_user = ""
    max_life_expectancy_user = float("-inf")

    for entity, life_expectancy in data_by_year[year]:
        if life_expectancy < min_life_expectancy_user:
            min_life_expectancy_user = life_expectancy
            min_life_country_user = entity

        if life_expectancy > max_life_expectancy_user:
            max_life_expectancy_user = life_expectancy
            max_life_country_user = entity

    # return the average life expectancy, the country with the min life
    # expectancy, and the country with the max life expectancy for the year
    return {
        "avg_life_expectancy": avg_life_expectancy,
        "min_life_expectancy_country": min_life_country_user,
        "min_life_expectancy": min_life_expectancy_user,
        "max_life_expectancy_country": max_life_country_user,
        "max_life_expectancy": max_life_expectancy_user
    }


# function to get the data for a country
def get_country_data(country, data_by_country):
    # check if the country is in the dictionary
    if country not in data_by_country:
        # if not, return None
        return None

    # get the life expectancies for the country
    country_data = data_by_country[country]

    # find the year with the highest and lowest life expectancy for the country
    # using a lambda function
    max_year_country = max(country_data, key=lambda x: x[1])
    min_year_country = min(country_data, key=lambda x: x[1])

    # return the year with the highest and lowest life expectancy for the
    # country
    return {
        "highest_life_expectancy_year": max_year_country[0],
        "highest_life_expectancy": max_year_country[1],
        "lowest_life_expectancy_year": min_year_country[0],
        "lowest_life_expectancy": min_year_country[1]
    }


# main function
def main():
    # define the filename path and load the data
    filename = 'Week6/life-expectancy.csv'
    (
        life_expectancies_by_year,
        life_expectancies_by_country,
        min_life_expectancy,
        min_life_country,
        min_life_year,
        max_life_expectancy,
        max_life_country,
        max_life_year
    ) = load_data(filename)

    # use a while true loop to allow the user to search multiple times
    while True:
        # ask the user if they want to search by year or country
        user_choice = input("Do you want to search by (Y)ear or (C)ountry? ")
        # strip and convert the user's choice to lowercase
        user_choice = user_choice.strip().lower()

        if user_choice == "y":
            while True:
                try:
                    user_year = int(input("Enter the year of interest: "))
                    year_data = get_year_data(user_year,
                                              life_expectancies_by_year)
                    if year_data:
                        break
                    else:
                        print(f"No data available for {user_year}")
                except ValueError:
                    print("Invalid year. Please enter a valid year.")

            print(f"The overall max life expectancy is:"
                  f" {max_life_expectancy:.3f} from {max_life_country} in"
                  f" {max_life_year}")
            print(f"The overall min life expectancy is:"
                  f" {min_life_expectancy:.3f} from {min_life_country} in"
                  f" {min_life_year}")

            print(f"\nFor the year {user_year}:")
            print(f"The average life expectancy across all countries was:"
                  f" {year_data['avg_life_expectancy']:.3f}")
            print(f"The max life expectancy was in"
                  f" {year_data['max_life_expectancy_country']} with"
                  f" {year_data['max_life_expectancy']:.3f}")
            print(f"The min life expectancy was in"
                  f" {year_data['min_life_expectancy_country']} with"
                  f" {year_data['min_life_expectancy']:.3f}")
        elif user_choice == "c":
            while True:
                user_country = input("Enter the country of interest: ")
                user_country = user_country.strip().capitalize()
                country_data = get_country_data(user_country,
                                                life_expectancies_by_country)
                if country_data:
                    break
                else:
                    print(f"No data available for the country {user_country}.")

            print(f"Country: {user_country}")
            print(f"The highest life expectancy was in"
                  f" {country_data['highest_life_expectancy_year']} in"
                  f" {country_data['highest_life_expectancy']:.3f} years.")
            print(f"The lowest life expectancy was in"
                  f" {country_data['lowest_life_expectancy_year']} in"
                  f" {country_data['lowest_life_expectancy']:.3f} years.")
        else:
            print("Invalid choice. Please enter 'Y' for year or 'C' for"
                  " country.")

        search_again = input("Do you want to search again? (Y/N): ")
        search_again = search_again.strip().lower()
        if search_again != "y":
            break


if __name__ == "__main__":
    main()
