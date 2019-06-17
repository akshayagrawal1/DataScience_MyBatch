# making your own module

def display():
    print('Hello')
    print('Name of called moudule is :', __name__)
    
string = 'Welcome to the world of Python !!!' # variable definition


def addition(a,b):
    """
    addition(a,b) which will return  a + b
    >>> my_module.addition(5,7)
    12
    """
    return a+b