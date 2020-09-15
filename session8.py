def check_fn_docs():
    '''
    A function check_fn_docs is defined to check whether the input function 
    has doctring length should be 50 characters.
    Input : function name
    Output : Bool
    '''
    char_count = 50
    def len_docs_chcek(func):
        '''
        Inner function of check_fn_docs.
        '''
        if len( func.__doc__ ) > char_count:
            return True
        else:
            return False
    return len_docs_check


def next_fibo_number():
    '''
    print the next fibonacci number
    Input : None
    Output : Int Type next fibonacci number
    '''
    a, b, count = 0, 1, 0
    def print_next_number():
        '''
        Inner function of next_fibo_number
        '''
        nonlocal a, b, count
        count += 1
        if count == 1:
            return 0
        elif count == 2:
            return 1
        else:
            c = a + b
            a, b = b, c
            return b
        count = count + 1
    return print_next_number


def add(a, b):
    '''
    A function add which take two input parameters.
    And add them if it is number 
    or concatenate them if it is a string.
    Input: a, b two parameters
    Output: a+b
    '''
    return a+b


def mul(a, b):
    '''
    A function mul which take two input parameters.
    And multiplies them if both are number
    or one parameter is string and second one is number then print string integer times
    Input: a, b two parameters
    Output: a*b
    '''
    return a*b



def div(a, b):
    '''
    A function mul which take two input parameters.
    And multiplies them if both are number
    or one parameter is string and second one is number then print string integer times
    Input: a, b two parameters
    Output: a/b
    '''
    return a/b

