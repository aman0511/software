def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    x=x%2
    return bool(x)
print odd(5)