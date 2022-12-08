principle = float (input("Enter the amount: "))
time = float (input("Enter time: "))
rate = float (input("Enter rate: "))

simple_interest = (principle*time*rate)/100
compound_interest = principle * ( (1+rate/100)**time - 1)

print('Simple interest is: %f' % (simple_interest))
print('Compound interest is: %f' %(compound_interest))