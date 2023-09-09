print('Please enter the following information: ')

# basic information for application ID
first = input('What is your first name? ')
last = input('What is your last name? ')
email = input('What is your email address? ')
phone = input('What is your phone number? ')
job_title = input('What is your job title? ')
id_number = input('What is your ID number? ')

# additional information for application ID
hair_color = input('What is your hair color? ')
eye_color = input('What is your eye color? ')
month = input('Starting month: ')
training = input('Completed additional training? ')

# print application ID
print('\nThe ID Card is:')
print('----------------------------------------')
print(f'{last.upper()}, {first.capitalize()}')
print(job_title.title())
print(f'ID: {id_number}\n')
print()
print(email.lower())
print(phone)
print()
print(f'Hair: {hair_color:15} Eyes: {eye_color}')
print(f'Month: {month:14} Training: {training}')
print('----------------------------------------')