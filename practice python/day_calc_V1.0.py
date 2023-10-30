# inputs
day = int(input('Insert day: '))
month = int(input('Insert month: '))
leap_year = input('Is it leap-year?(yes/no): ')

# set up calc
x = 365 / 12

# calcs
if leap_year.upper() == 'YES':
    if month == 1:
        number = day
    elif month == 2:
        number = day + 31
    elif month >= 3:
        number = day + (month - 2) * x + 28
elif leap_year.upper() == 'NO':
    if month == 1:
        number = day
    elif month == 2:
        number = day + 31
    elif month >= 3:
        number = day + (month - 2) * x + 28
else:
    print('error')

# Finis
print('Days passed:', number, '/ 365')