def addition(a,b):
    """
    This function will add two number and syntax is srikanth.addition(a,b) 
    will return a + b
    
    >>> srikanth.addition(5,7)
    12
    
    """
    return a+b


def fibonacci_series(start,length):
    """
    In mathematics, the Fibonacci numbers are the numbers in the following integer sequence,
    called the Fibonacci sequence, and characterized by the fact that every number after the first 
    two is the sum of the two preceding ones:
    
    1 1 2 3 5 8 13 21 ...
    
    syntax: fibonacci_series(start, length) will return fibonacci_series in selected range and starting number
    
    >>> fibonacci_series(1,8)
    1 1 2 3 5 8 13 21 
    """
    print('Your are currently working in module  - "{}"'.format(__name__))
    
    # initializing values in 
    n1 = 0
    n2 =start
    i = 0
    while i < length:
        print(n2,end=',')
        nth = n2
        n2 = nth + n1
        n1 = nth
        #n2= nth+n2
        i += 1 
        
    print('\b')
    raise ValueError('Fibonacci Series generate few value')
        
        
        
        
        
        