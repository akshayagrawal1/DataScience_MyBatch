def create_dir(path):
    """
    Srikanth.create_dir is a function used to create a folder in a
    specified path
    >>> import srikanth
    >>> srikanth.create_dir(Foldername)

    """
    import os
    os.mkdir(path)

def iseven(num):
    try:
        if num % 2 == 0:
            print('{} is even'.format(num))
        else:
            print('{} is odd'.format(num))
    except (TypeError,ValueError):
        print('Excepted Integers but got float or strings')

def fibanocci_series(start,count):
	