balance1=balance
monthlyinterestRate=annualInterestRate/12
lowest=0
while balance1>lowest:
    month=1
    balance=balance1
    while month<=12:
        unpaidbalance=balance-lowest
        interest=unpaidbalance*monthlyinterestRate
        balance=interest+unpaidbalance
        month=month+1
    if balance>0:
           lowest=lowest+10
    else :
        break
            
print "Lowest Payment: "+str(lowest)