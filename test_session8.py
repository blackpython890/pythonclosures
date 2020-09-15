import pytest , os , inspect
import re , random, session8


README_CONTENT_CHECK_FOR = ['check_fn_docs',
                            '__doc__',
                            'next_fibo_number',
                            'mul',
                            'add',
                            'div',
                            'function_counter'
                            ]


#1 README Exists
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


#2 README Formatting
def test_readme_for_formatting():
    readme = open('README.md','r')
    content = readme.read()
    readme.close()
    assert content.count('#') >= 5 , "Kindly format the README.md"


#3 README Words  Count
def test_readme_words_counts():
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100 , "Kindly define README properly"


#4 Readme Proper Description
def test_readme_proper_desscription():
    READMELOOKSGOOD = True
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    for words in README_CONTENT_CHECK_FOR:
        if words not in readme_words:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True , "You have not defined all functions/classes in README.md"


#5 function name had caps letter
def test_funcation_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction )
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


#6 PEP8 Guidelines
def test_fourspace():
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0,"Your code intentation does not follow PEP8 guidelines" 


#7 check docstring exist
def test_docstring_length():
    a = session8.check_fn_docs()
    assert a(session8.mul) == True


#8 check next fibonacci number
def test_fibonacci():
    k = session8.next_fibo_number()
    k()
    k()
    k()
    assert k() == 2


#9
def test_function_single_dict_call():
    c = session8.function_counter( session8.add )
    c()
    c()
    c()
    c = session8.function_counter( session8.mul )
    c()
    c = session8.function_counter( session8.div )
    c()
    k = c()
    assert k == {'add': 3, 'div': 2, 'mul': 1}



#10
def test_function_calling_sep_dict():
    c = session8.function_two_dict(session8.add, session8.userA)
    c()
    c()
    l = session8.function_two_dict(session8.mul,session8.userA)
    l()
    l()
    x = session8.function_two_dict(session8.div,session8.userA)
    x()
    x()
    c = session8.function_two_dict(session8.add,session8.userB)
    c()
    c()
    c()
    l = session8.function_two_dict(session8.mul,session8.userB)
    l()
    x = session8.function_two_dict(session8.div,session8.userB)
    x()
    x()
    assert session8.userA == {'add': 2, 'div': 2, 'mul': 2} and session8.userB == {'add': 3, 'div': 2, 'mul': 1}