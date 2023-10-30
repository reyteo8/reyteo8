# inputs
day = int(input('Insert day: '))
month = int(input('Insert month: '))
leap_year = input('Is it leap-year?(yes/no): ')

# set up calc
x = 365 / 12

# calcs
if leap_year.upper() == 'yes':
    if month == 1:
        number = day
    if month == 2:
        number = day + 31
    if month == 3:
        number = day + 31 + 29
if leap_year.upper() == 'no':
    if month == 1:
        number = day
    if month == 2:
        number = day + 31
    if month >= 3:
        number = day + (month - 1) * x
else:
    print('error')
# Finis
print('Days passed:', number, '/ 365')