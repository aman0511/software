balance=400000
balance1=balance
annualInterestRate=.14
Monthly_interest_rate = (annualInterestRate) / 12.0
lower_bound = balance / 48
upper_bound = (balance *(1 + Monthly_interest_rate)**48) / 12.0
while(abs(balance)>0.01):
    balance=balance1
    lowest=(lower_bound+upper_bound)/2
    month=1
    while month<=48:
        unpaidbalance=balance-lowest
        interest=unpaidbalance*Monthly_interest_rate
        balance=unpaidbalance+interest
        month=month+1
    if balance>.01:
        lower_bound=lowest
    else :
        upper_bound=lowest
   # print str(balance)+" "+str(lowest)
print "Lowest Payment: "+str(round(lowest,2))