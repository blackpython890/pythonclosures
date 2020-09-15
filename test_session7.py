import pytest, os, inspect, re, random, session7
from functools import partial, reduce


#1 Test Biggest character as per ASCI value
def test_biggest_asci_character():
    k = reduce(lambda a,b :a if a > b else b, [x for x in 'tsai'])
    assert k == 't'


#2 Vowel Strip
def test_vowel_strip():
    l = "tsai"
    k = [i for i in l if i not in ('a','e','i','o','u','A','E','I','O','U') ]
    s = "".join(i for i in k)
    assert s == 'ts'


#3 ReLU Implementaton
def test_relu_function():
    a = [-2, -1, 0, 1, 3, -4, 5]
    k = [i if i>0 else 0 for i in a]
    assert k == [0, 0, 0, 1, 3, 0, 5]


#4 Add iterables
def test_add_iterables():
    a = [1,2,3,4,5,6]
    b = [10,9,4,13,11,17]
    d = [(x+y) for x in a if x%2==0 for y in b if y%2!=0 ]
    assert d == [11, 15, 13, 19, 13, 17, 15, 21, 15, 19, 17, 23]


#5 Sigmoid Implementaton
def test_sigmoid_function():
    a = [-2,-3,2,3,4]
    k = [1 if i>=1 else 0 for i in a]
    assert k == [0, 0, 1, 1, 1]


#6 Test Shift Characters
def test_shift_characters():
    a = "tsai"
    k=[chr(ord(i)+5) for i in a]
    p = "".join(i for i in k)
    assert p == 'yxfn'


#7 Number plate generation
def test_random_number_plate():
    z = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    s = ["KA" + str(random.randint(11,98)) + str(random.choice(z)) + str(random.choice(z)) + str(random.randint(1001,9998)) for i in range(15)]
    assert type(s) is list


#8 Number plate genration using partial
def test_number_plate_partial():
    f = partial(session7.numberplate, b=1011 )
    k = f('DL')
    assert type(k) is list


#9 
def test_reduce_add_even_number_():
    s=reduce(lambda a,b:(a+b),session7.generate_even_number_list())
    assert s == 30


# 10
def test_reduce_add_every_third():
    s=reduce(lambda a,b:(a+b),session7.generate_every_thirdelement_list())
    assert s == 22
