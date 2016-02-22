
# This program displays gross pay

# Get the number of hours worked
hours = float(input('Enter the hours worked this week: '))
# making sure hours are greater than 0 and less than 60
count = 0
while (0 > hours or hours > 60):
    hours = float(input('Enter the hours worked this week: '))
    count = count + 1

# Get the hourly pay rate
pay_rate = float(input('Enter the hourly pay rate: '))

# Making sure pay_rate is greater than 0 and less than 20 hours
while (0 > pay_rate or pay_rate > 20):
    pay_rate =  float(input('Enter the hourly pay rate: '))
    count = count + 1

# Calculate the gross pay
gross_pay = hours * pay_rate

# Display the gross pay
print('Gross pay: $', format(gross_pay, ',.2f'))





