def add(a, b):
    '''
    A function add which take two input parameters.
    And add them if it is number 
    or concatenate them if it is a string.
    Input: a, b two parameters
    Output: a+b
    '''
    return a+b
    add_count()


def mul(a, b):
    '''
    A function mul which take two input parameters.
    And multiplies them if both are number
    or one parameter is string and second one is number then print string integer times
    Input: a, b two parameters
    Output: a*b
    '''
    return a*b
    mul_count()



def div(a, b):
    '''
    A function mul which take two input parameters.
    And multiplies them if both are number
    or one parameter is string and second one is number then print string integer times
    Input: a, b two parameters
    Output: a/b
    '''
    return a/b
    div_count()


def function_counter(func):
    count = 0
    def start_count():
        nonlocal count
        count += 1
        def print_coun
        t():
            print('{0} function is called {1} times.'.format(func.__name__,count))
        return print_count
    return start_count



add_count = function_counter(add)
mul_count = function_counter(mul)
div_count = function_counter(div)