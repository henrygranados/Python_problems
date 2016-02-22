def print_investment(investment, interest_rate, years):
    amount = investment

    for yr in range(years):
        amount = (amount) * (1. + interest_rate)
        print('After {:>2d} year{} you have:   $ {:>10.2f}'.format(yr + 1, 's,' if yr > 0 else ', ', amount))


number_of_tries = 5
for idx_try in range(number_of_tries):
    print("===== Investment " + str(idx_try + 1))

    while True:
        investment = float(input('Enter your initial investment: '))
        if 1000 <= investment <= 100000:
            break
        else:
            print("Investment must be between $1,000 and $100,000")

    while True:
        interest_rate = float(input('Enter your anual interest rate (%): '))  # this already ensures float
        if 0 <= interest_rate <= 10:
            break
        else:
            print("The anual interest rate must be between 0 and 10") # interest rate must be between 0 and 10
    
    interest_rate /= 100.0

    while True:
        years = int(input('How many years should I calculate?: ')) 
        if 0 <= years <= 10:
            break
        else:
            print("Years must be between 0 and 10")  # years must be between 0 and 10

    
    print_investment(investment, interest_rate, years)
