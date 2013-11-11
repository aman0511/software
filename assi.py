balance=float(raw_input())
annualInterestRate=.2
monthlypaymentrate=.04
monthlyinterestRate=annualInterestRate/12
month=1
total=0
while month<=12:
    minpayment=balance*monthlypaymentrate
    total=total+minpayment
    unpaidbalance=balance-minpayment
    interest=unpaidbalance*monthlyinterestRate
    balance=interest+unpaidbalance
    print "Month: "+str(month)
    print "Minimum monthly payment: "+str(round(minpayment,2))
    print "Remaining balance: "+str(round(balance,2))
    month=month+1
print "Total paid: "+str(round(total,2))
print "Remaining balance: "+str(round(balance,2))