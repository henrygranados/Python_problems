while True:
    investment = float(input('Enter your initial investment: '))
    if 1000 <= investment <= 100000:
        break
    else:
        print("Investment must be between $1,000 and $100,000")


#Annual interest rate 
apr = 3.0 / 100.0
yr = 1
amount = investment

for yr in range(1,6):
        amount = (amount) * (1. + apr)
        print('After {:>2d} year{} you have:   $ {:>5.2f}'.format(yr, 's,' if yr > 1 else ', ', amount))

print('\nThe initial investment was: ', investment)
print('The final value of the investment after five years is $ {:>5.2f}'.format(amount))

