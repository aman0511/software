lower=0
upper=0
def isIn(char, aStr):
    
    upper=len(aStr)
    lower=0;
   
    while True:
        print aStr
        root=(upper+lower)/2
        if upper==lower:
            return False
        elif char==aStr[root] :
            return True
        elif char>aStr[root]:
           isIn(char, aStr[root:])
           
        else:
           isIn(char, aStr[:root])
 
print isIn('k', 'abcfinw')
           