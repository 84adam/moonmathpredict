# Based on https://www.moonmath.win/

# Current price in USD
price = 3400
# Compound Daily Periodic Rate (modified weighted average based on years 2010-2017)
rate = 0.2406

def compound_interest(principle, rate, time): 
    # Calculates compound interest 
    CI = principle * (pow((1 + rate / 100), time)) 
    return CI

print("\tTime Span: \tBTC Price Prediction: ")

# daily compounding, prediction for each year in advance, going out 10 years
for i in range((1*365),(11*365)):
    if i % 365 == 0:
        print("\t {0:>2} years \t${1:>11,.0f}".format(int((i/365)), compound_interest(price, rate, i)))
