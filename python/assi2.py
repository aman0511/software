balance=int(raw_input())
annualInterestRate=float(raw_input())
monthlyinterestRate=annualInterestRate/12
lowest=0
while balance>lowest:
    month=1
    while month<=12:
        unpaidbalance=balance-lowest
        interest=unpaidbalance*monthlyinterestRate
        balance=interest+unpaidbalance
        month=month+1
    print str(balance)+" "+str(lowest)
    if balance>lowest:
           lowest=lowest+10
    else :
        break
            
print lowest