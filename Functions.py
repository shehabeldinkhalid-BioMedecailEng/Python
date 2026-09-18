# How to make a function
def My_function():
  print("Hello from a function")
My_function()
# parameters
def multiply(number):
  for X in range(11):
   print(f"{number}x{X}={number*X}")
# function and return
def functionname():
    print("python from inside function")

# call function
functionname()

def shehab():
    return " 19 My age "

person=shehab() # return a function
print(person)

# parameter
def Say_hi(Name):  
    str(Name)      # task
    print(f"HI {Name}") # task
    return Name   # return
frist_name = Say_hi("shehab") # argument
second_name = Say_hi("Ahmed")  # argument
print(type(frist_name))
print(second_name)


def addition(a , b):
    if type(a) == int or type(b) == int :
        print(a + b)

        
addition(5,6) # 11
addition('a','b') #
addition(3,True) # 4 


def Name(Frist , Middle , Last):
    print(f"{Frist.strip().capitalize()} {Middle.strip()} {Last.strip()}")

Name("   shehab","       khalied    ","     hamed     ")


# using packing and unpacking
def Say_hi(*peapols):    # packing
    for person in peapols:   # unpacking
        print(f"Hi {person}")
    return peapols

peapols = Say_hi("shehab","sara","khalied","mohamed","tark")

for X in range(len(peapols)):
    print(f"Talk about your self {peapols[X]}")


# defult parameter
def person(Name="shehab" ,age=19,work="Eng"):
    print(f"{work.strip().capitalize()} {Name.strip().capitalize()} his age is {age}")

person("faroq","12")

#Function Packing Unpacking Keyword Arguments
def Skills(*skills):         # make Packing and Unpacking array
    print(type(skills))
    array_skills=[]
    for skill in skills:
        array_skills.append(skill)
        print(f"Good you finished {skill}")        
    print(f"Good you finished all of this {array_skills}")
  
Skills("python","HTML","CSS","MTCP","WEBD","C++","C")       

def Skills(**skills):         # make Packing and Unpacking dictionary
    print(type(skills))
    for number,skill in skills.items():
        print(f"Good you finished {number} {skill}")        
          
Skills(Frist="python",Second="HTML",Third="CSS",Fourth="MTCP")  

# dictionary 
skills={
    'Frist':"python",
    'Second':"HTML",
    'Third':"CSS",
    'Fourth':"MTCP"
}
Skills(**skills)  # you must use the unpacking and packing using **


# function scope

# Global scope 
X = 1
print(X)   # <--- Global scope

# local scope
def Num():
    X=2    # <--- local scope
    print(X)

Num()

def num():
    global x
    x = 6
    print(x)    

num() # you must to call the function before global x
print(x)

# function recertion call itself inside
def factorial(x):
    # """This is a recursive function
    # to find the factorial of an integer"""

    if x == 1:         # condition
        return 1
    elif x == 0:       # condition
       return 0
    else:
      return (x * factorial(x-1))

 
num = 3
print("The factorial of", num, "is", factorial(num))


# lambda function
X = lambda name : f"HI {name}"
#======================================================================================#
    
# Dicorators 
def Decorator(Func):
    def nestedFunc(Name):
        print("Before Function")   
        Func(Name)                       # Function that used as parameter
        print("After Function")
    return nestedFunc              # return Dara 
@Decorator
def say_hallow(Name):
    print(f"Hi {Name} ")

say_hallow("shehab")
# afterDecoration = Decorator(say_hallow("shehab"))
# afterDecoration()

# Generators
def MyGenerators():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    
X = MyGenerators()      # without using iter() function 

print(type(MyGenerators))   # Function
print(MyGenerators())       # Generator
print(40 * "=")
print(next(X) , end=" ")
print(next(X) , end=" ")
print(next(X) )

for i in X:   # Donot start from begiaing 
    print(i)
    
# ----- Type Hinting ----------------
def sayhi(Name) -> str : # Hint the parameter must be str 
    print(f"Hello {Name}")
    
sayhi("shehab")
sayhi(10)

R = ["A","B","C","D","E","F"]
def hintlist(X) -> list:  # Hint that it take array and list
    Y=0
    for i in X:
        Y+=1
        print(f"The item number {Y} is {i}")

hintlist(R)
hintlist("ahmed")
