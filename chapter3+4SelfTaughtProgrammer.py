

#Chapter 3 Self Taught Programmer

"""print three string"""


print("I love cheese")
print("I love water")
print("I love coffee")


"""write a program that prints a message if a varibale is less than 10
and different message if the varibale is greater than or equal to 10"""

def choose_numb(i):
    if i < 10:
        print("heck yes")
    elif i >= 10:
        print("yes")
    else:
        print("no")
    


"""write a program that prints a message if a varibale is less than or equal to
10,another mesage if the variable is greater than 10 but less than or equal
to 25, and another message if the variable is greater than 25"""
def choose_numb2(i):
    if i <= 10:
        print("heck yes")
    elif i > 10 <= 25:
        print("yes")
    elif i > 25:
        print("ok")
    else:
        print("no")

"""create a program that divides two variables and prints the remainder"""
def mod_oper(a,b):
    return a%b
    print(a%b)



"""create a program that takes two variables, divides them and prints the
quotient """

def quot(a,b):
    return a/b
    print(a/b)

"""write a program with a variable 'age' assigned to an integer that prints
different strings depending on what integer 'age' is"""
def age(i):
    if age <= 25:
        print("too young")
    elif age > 25 and age <= 30:
        print("perfect")
    else:
        print("do you have a younger brother")
    

####Chapter 4

"""1. write  a function that takes a number as input and returns that number
squared"""
def square_bob(x):
    return x**2

# print(square_bob(4))
#16


"""2. create a function that accepts a string as a paramater and prints it"""
def print_string(string):
    print(string)
##>>> print_string("problem two")
##problem two
##>>> 

"""3. write a function that takes three parameters and two optional params"""
def problem_three(x, y, z, a=10, b=12):
    return x + y + z + a + b

result = problem_three(5, 7, 9)
print(result)


"""4. write a program with two functions. The first function should take an
integer as a parameter and return the result of the integer divided by 2,
the second function should take an integer as a parameter and return the
result of the integer multiplied by 4. call the first function , save
the result as a variable, and pass it as a parameter to the second function"""

def cat(u):
    return u/2

def dog(d):
    return d*4

x = cat(80) 
quad = dog(x)
print(quad)


"""5.write a function that converts a string to a float and returns the result"""

def convert(str):
    try:
        return float(str)
    except ValueError:
        print("Could not convert the string to a float")



    
