from functools import reduce


def normalize(name):
    return str.capitalize(name)
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print L2
# def char2num(s):
#     return {'0':0, '1':1, '2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# def prod(L):


def prod(L):
    return reduce(lambda x, y: x*y, L)
print ("sum is ", prod([3, 5, 7, 9]))

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2float(s):
    return reduce(lambda x, y, z, map(char2num, s))
print (str2float('123.456'))