"""
import pickle

# Pickling a python object

cars = ["Audi","BMW","Swift","Harryti Tuzuki","Porche"]
file = "mycar.pkl"
fileobj = open(file, 'wb')
pickle.dump(cars,fileobj)
fileobj.close()


file = "mycar.pkl"
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
print(mycar)
"""

def my_generators():
    for i in range(5000):
        #complex computations
        yield i

gen = my_generators()
"""print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def set_list(list):
    list = ["A","B","C","D"]
    return list

def add (list):
    list.append("E")
    return list

my_list = ["F"]
print(set_list(my_list))
print(add(my_list))


def gen(n):
    for i in range (n):
        yield i

ob1 = gen (4)

print(next(ob1))
print(next(ob1))
print(next(ob1))

num = "ROHIT SHARMA"
iter1 = iter(num)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

string = "MY IDOL IS ROHIT SHARMA"
string_list = string.split(' ')
print(string_list)
print(' '.join(string_list))

def prac_function( **kwargs):

    for key, value in kwargs.items():
        print(key,value)

prac_function(Name='ROHIT', Age=36, City='MUMBAI',Captain='INDIAN CRICKET TEAM')
"""


def funargs(*args,**kwargs):
    for item in args:
        print(item)
        print("I INTRODUCA MY IDOL")
    for key, value in kwargs.items():
        print(f"{key}is {value}")

har = ["MANASI","MOHAN","PATIL"]
kw= {"Name":"ROHIT,"Age":"36","Captain":"Indian Cricket Team"}
funargs(*har **kw)
