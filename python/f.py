#result=1.00
def iterPower(base, exp):
    result=1.00
    while exp>0:
         
         result=result*base
         exp=exp-1
    return result
        
print iterPower(2, 3)