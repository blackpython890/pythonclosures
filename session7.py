import random


numbers = range(10000)

# function that filters vowels
def filterFibnocci(number):
    a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    if(number in a):
        return True
    else:
        return False


def numberplate(state_code, const):
    alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    plate_no = [ state_code + str(random.randint(11,98)) + str(random.choice(z))+ str(random.choice(alp)) + str(const) for i in range(15)]
    return plate_no


def generate_even_number_list():
    k = []
    for i in range(1,11):
        if i%2==0:
            k.append(i)
    return k


def generate_every_thirdelement_list():
    k = []
    s = [1,2,3,4,5,6,7,8,9,10]
    for i in range(0,len(s),3):
        k.append(s[i])
    return k
