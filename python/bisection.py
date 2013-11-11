print "please think of a number between 0 and 100"
low=0
high=100

while True:
    ans=(0+100)/2
    print "Is your secert numer "+str(ans)+"?" 
    value=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.");
    if value=='h':
        low=ans
    if value=='l':
        high=ans
    if value=='c':
        break
print "Game over. Your secret number was: "+str(ans)