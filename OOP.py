"""
If I need to create an application, we will use lots of buttons for sure,
these buttons can be created following two paradigms (ways): procedural or object-oriented

"""


# 1-  Procedural paradigm:

def button1Clicked():
    print("do some action")


def button2Clicked():
    print("do some action")


def button3Clicked():
    print("do some action")


def button4Clicked():
    print("do some action")


button1_color = "green"
button1_size = "60 * 30"
button1_active = True
button1Clicked()

button2_color = "green"
button2_size = "60 * 30"
button2_active = True
button2Clicked()

button3_color = "green"
button3_size = "60 * 30"
button3_active = True
button3Clicked()

button4_color = "green"
button4_size = "60 * 30"
button4_active = True
button4Clicked()

"""
The procedural paradigm is not efficient when you need to make many instances (copies, objects)
of the same class (category: ex. button)
"""

# 2-    Object-oriented paradigm:
"""
this technique relies on classes, you create single class and copy multiple
instances of this class, just create a class called button and make as many button as you need 
from this class, without the need to rebuild each button from scratch.
"""


class button_class:
    """
    this is the class (category) of all buttons in the application you want to build
    """


button1 = button_class()
button2 = button_class()
button3 = button_class()
button4 = button_class()

"""
But where to add the attributes (color, size, ..) and methods (actions or functions)?
Due to the fact that classes are built to take copies from them, all data and function are put inside the class.
"""


class button_class:
    """
    colorVariable = color
    sizeVariable = size
    isActiveVariable = boolean

    """


"""
then when you need to make a new button you take a copy (object or instance) from that class and add values to those predefined variables
according to each button
"""

"""
ex:
button1 = button_class("green", "30 * 40", True)
button2 = button_class("red", "70 * 40", False)
button3 = button_class("blue", "10 * 20", True)

"""

"""
but how to add those variables in the class?
variables (attributes) are added using the __init__ method which take those variables (attributes)
as parameters after the self parameter .
"""


class button_class:
    """
    colorVariable = colorValue
    sizeVariable = sizeValue
    isActiveVariable = booleanValue

    """

    def __init__(self, colorValue, sizeValue, isActiveValue):
        # "button"  "variable"    "value"
        self.colorVariable = colorValue
        self.sizeVariable = sizeValue
        self.activeVariable = isActiveValue
        # those are attributes (data of the class)


button1 = button_class("green", "30 * 40", True)
button2 = button_class("red", "70 * 40", False)
button2 = button_class("blue", "10 * 20", True)

"""
how to add actions to class?
always add actions in a function not in the outer class scope, as it will be performed
during class definition not when creating an object

"""

# don't do that

class button_class:
    def __init__(self, colorValue, sizeValue, isActiveValue):
        # "button"  "variable"    "value"
        self.colorVariable = colorValue
        self.sizeVariable = sizeValue
        self.activeVariable = isActiveValue

    print(3 + 1)

# instead,  do that

class button_class():
    def __init__(self, colorValue, sizeValue, isActiveValue):
        # "button"  "variable"    "value"
        self.colorVariable = colorValue
        self.sizeVariable = sizeValue
        self.activeVariable = isActiveValue
    def calculate(self):  # this is called a method, you can add as many methods as you need
        print(3 + 1)
    def buttonClicked(self):
        print("button is clicked")


# in-lab example
# -----------------------------------
class person:
    def __init__(self, name, job, age, married):
        self.name = name
        self.job = job
        self.age = age
        self.marriedOrnot = married
    def talk(self):
        return  "i am talking now"

doctor = person("ahmed", "doctor", 30, True)


print(doctor.age)
print(doctor.talk())

## -------------------------------------------------------------



"""
The object-oriented paradigm has 4 concepts:
1- Encapsulation
2- Abstraction
3- Inheritance
4- Polymorphism
"""

# 1- Encapsulation:
"""
We have already seen a side of encapsulation which means to encapsulate (bundle) all data (attributes) and actions (methods)
inside the class. So when needed to access to some value like colorValue we can't access it directly as it is privately bundled 
inside the class.
"""
# we can't do that
my_button = button_class("red", "30*60", 0)
# print(colorVariable)


"""
we have to indicate that the colorValue is inside the class button_class to be able to access it
"""
# we have to do that
print(my_button.colorVariable)
"""
The same applies for methods
"""

# can't do that

# calculate()

# but u have to do that

my_button.calculate()

"""
note: you can access class methods in 2 ways:
1- class_name.method(object_name)
2- object_name.method()

"""

button_class.calculate(my_button)
my_button.calculate()

"""
the bundling or hiding was the first side in the encapsulation concept,
the second part in encapsulation meaning is that you can restrict access
or modifications to those attributes by making them private to setter and getter functions.
we make variables to be private by starting them with double underscores
"""


class ButtonClass:
    def __init__(self, colorValue, sizeValue, isActiveValue):
        # Initialize private attributes
        self.__color = colorValue
        self.__size = sizeValue
        self.__isActive = isActiveValue

    # Getter method for color
    def get_color(self):
        return self.__color

    # Setter method for color
    def set_color(self, colorValue):
        self.__color = colorValue

    # Getter method for size
    def get_size(self):
        return self.__size

    # Setter method for size
    def set_size(self, sizeValue):
        self.__size = sizeValue

    # Getter method for isActive
    def is_active(self):
        return self.__isActive

    # Setter method for isActive
    def set_active(self, isActiveValue):
        self.__isActive = isActiveValue

    # Method to perform some action
    def calculate(self):
        print(3 + 1)

    # Method to handle button click
    def button_clicked(self):
        print("Button is clicked")


button = ButtonClass("red", "large", True)
print(button.get_color())  # Accessing private attribute through getter
button.set_color("blue")  # Modifying private attribute through setter
print(button.get_color())

# 2- Abstraction

"""abstraction focuses on the ease of use, or making it simple to use the class methods, for instance, when u use a 
remote controller, you don't care about what inside, but you only focus on clicking on the outer buttons and the 
controller does its function
Same in classes, we don't care about how the calculate method is implemented, but we can simply use it.
"""


# Part ====> 1
# OOP paradigm or coding style 
# Class syntax and info
class shehab:
    def __init__(self) -> None: # create object (constractor)
        print("A new member has been added")  

# Call class
shehab()
shehab()
# To what inside 
print(dir(shehab)) 
CLASS = shehab
CLASS1 = shehab()
print(CLASS.__class__)
print(CLASS1.__class__)
print("="*30)

# Part ====> 2
# Attributes 
class Belal:
    names_notAllowed = ["Shit","Baloot","Fuck","Pitch"] # Class attrributes
    def __init__(self,name,Long,wide) -> int:
        self.YOUR_long = Long                          # Construct attrributes
        self.YOUR_wide = wide                          # Construct attrributes
        self.name = name.strip().lower().capitalize()  # Construct attrributes
        if self.name in  Belal.names_notAllowed  :
            raise NameError("sorry that name is not allowed")
        pass
    
print(Belal("shehab","178 CMeter","36 CMeter").YOUR_long +" "+ Belal("shehab","178 CMeter","36 CMeter").YOUR_wide)
try:
    print(Belal("fuck","178 CMeter","36 CMeter").name)
except:
    print("It Gives error")
    
# Class Attributes counter
class Mohamed:
    counter_users = 0
    def __init__(self , WhatYouKnow ) -> str:
        self.info = WhatYouKnow
        Mohamed.counter_users += 1
    def Remove(num) -> int :
        Mohamed.counter_users -= int(num)

         
print(Mohamed.counter_users) # Before counting
One = Mohamed("Allah slave") # 1
Two = Mohamed ("Massenger")  # 2
Third = Mohamed("From Maka") # 3
print(Mohamed.counter_users) # After counting
Mohamed.Remove(3)            # Removing
print(Mohamed.counter_users) # After removing


print("="*30)


# Part ====> 3
# Methods
class Zizo:
    king = "SHEHAB"
    def __init__(self , NAME , AGE , Friend , gender) -> str:
        self.YOUR_NAME = NAME
        self.YOUR_AGE = AGE
        self.friend = Friend
        self.gender = gender.strip().lower().capitalize()
        pass
    # FRIST Method
    def full_details(self):       # Instance method
        return f"Your name is {self.YOUR_NAME} and your age is {self.YOUR_AGE}"
    # Second Method
    def HI(self):                 # Instance method
        if self.gender == "Female":
            return f"HI Mrs {self.YOUR_NAME}"
        elif self.gender == "Male":
            return f"HI Mr {self.YOUR_NAME}"
        else:
            raise ValueError("choose Male or Female only if you are gay that is your proplem") 
    def JOE(self) -> str:         # Instance method
        print(f"Makes friend with {self.friend}")
    def Ibrahim(Play) -> str:     # Instance method
        print(f"Love to play {Play}")
    def Mero(self , Love) -> str: # Instance method
        print(f"{self.YOUR_NAME} Fall in LOVE with {Love}")
    # Class method
    @classmethod
    def ClassMethod(cls) -> str:
        print(f"Hi {cls.king} from Class Method")
    # Static method
    @staticmethod
    def Hello():
        print("Hello from static method")
        

# Call the Method 
print(Zizo("shehab",12, "jeo","male").Mero("eman"))
print(Zizo("reem",12, "jeo","   fEMaLe      ").HI())
print(Zizo("Mohamed",12, "jeo","   mALe      ").HI())
try:
    print(Zizo("neno",7, "jeo","dog").HI())
except ValueError:
   print("Value Error maybe you wrote some thing wrong") 
print(Zizo.ClassMethod())
print(Zizo.__class__) # info about the class and objects

# 3- Inheritance
"""
Inheritance is a key concept in Object-Oriented Programming (OOP) that allows a new class 
(known as a subclass or derived class) to inherit attributes and methods from an existing class (known as a superclass or base class). 
 This mechanism promotes code reusability and establishes a natural hierarchy between classes.
"""


# Base class (Super class)
class Button:
    def __init__(self, colorValue, sizeValue, isActiveValue):
        self.__color = colorValue
        self.__size = sizeValue
        self.__isActive = isActiveValue

    # Getter and Setter methods for color
    def get_color(self):
        return self.__color

    def set_color(self, colorValue):
        self.__color = colorValue

    # Getter and Setter methods for size
    def get_size(self):
        return self.__size

    def set_size(self, sizeValue):
        self.__size = sizeValue

    # Getter and Setter methods for isActive
    def is_active(self):
        return self.__isActive

    def set_active(self, isActiveValue):
        self.__isActive = isActiveValue

    # Base method
    def click(self):
        print("Button is clicked")


# Derived class (Sub class)
class ToggleButton(Button):
    def __init__(self, colorValue, sizeValue, isActiveValue, toggleState):
        super().__init__(colorValue, sizeValue, isActiveValue)
        self.__toggleState = toggleState

    # Getter and Setter methods for toggleState
    def get_toggle_state(self):
        return self.__toggleState

    def set_toggle_state(self, toggleState):
        self.__toggleState = toggleState

    # Overriding the click method
    def click(self):
        super().click()  # Call the base class method
        print(f"Toggle state is now {self.__toggleState}")


# Example usage:
button = ToggleButton("blue", "medium", True, "on")
print(button.get_color())  # Accessing inherited method
button.set_color("green")  # Modifying inherited attribute
print(button.get_color())
button.click()  # Using overwrite method
# Inhertance
class Food:
    def __init__(self,name,price,count):
        self.count = count
        self.price = price
        self.name = name
        print(f"{name} is created From Main class")
    def eat(self):
        print(f"Eat {self.name} Method from Main class")
    
class Apple(Food):
    def __init__( self , name , price , count , amount) -> str:
        # self.count=count           # ====>  attribute name
        # Food.__init__(self,price, count ,name)  # create instance from Main class
        super().__init__(name , price , count)     # Good practice way
        self.amount = amount
        print(f"{self.name} is created From Derived class")
        print(f"The price is {self.price}")
        print(f"The count {self.count}")
    def eat(self):
        return super().eat()    # method overwrite
food_one = Food
food_two = Apple("pizza","23$","4" ,"30")
print(food_two)

# Multiple inhertance
class Baseone:
    def __init__(self):
        print("Baseone")
        
    def func_one(self):
        print("One")
        
    

class Basetwo:
    def __init__(self):
        print("Basetwo")
    
    def func_two(self):
        print("Two")
        
class Derived(Baseone , Basetwo):
    pass

Myvar = Derived()     # frist instance only
print(Derived.mro())  # info about order

var = Derived
var1 = Derived.func_two(self="")  
var1 = Derived.func_one(self="")


# Part ====> 4
# 4- Polymorphism

"""
To illustrate polymorphism, let's build on the example of the Button class and its derived classes. We can create multiple subclasses that override a common method (e.g., click()), and then use polymorphism to treat them as instances of the same class.
"""


# Base class -> (super class)
class Button:
    def __init__(self, colorValue, sizeValue):
        self.color = colorValue
        self.size = sizeValue

    def click(self):
        raise NotImplementedError("Subclasses should implement this!")


# Subclass 1
class ToggleButton(Button):
    def click(self):
        print(f"Toggle button clicked. Color: {self.color}, Size: {self.size}")


# Subclass 2
class RadioButton(Button):
    def click(self):
        print(f"Radio button clicked. Color: {self.color}, Size: {self.size}")


# Subclass 3
class SubmitButton(Button):
    def click(self):
        print(f"Submit button clicked. Color: {self.color}, Size: {self.size}")


# Function to demonstrate polymorphism
def test_click(button):
    button.click()


# Example usage:
buttons = [ToggleButton("blue", "medium"), RadioButton("green", "small"), SubmitButton("red", "large")]

for button in buttons:
    test_click(button)  # Each button is treated as a Button, but behaves according to its specific class


# -----------------------------------------------------------------------------------------------------------------
class A :
    def DoSomething(self) -> None:
        print("From class A")

class B(A):
    def DoSomething(self) -> None:    # over write
        print("From class B")

my_instance = B()
my_instance.DoSomething()


# Part 5 ==> Decorator and setter and getter
class ALL:
    def __init__(self,NAME,AGE):
        self.__Name = NAME
        self.__Age = AGE
    def get(self):
        return self.__Name , self.__Age 
    def set(self,newName,newAge):
        self.__Name = newName  
        self.__Age = newAge

CV = ALL("shehab","18")
print(CV.get())
CV.set("SHEBA","19")
print(CV.get()) 

# Part 6 ==> ABCs ===> Abstract base class
from abc import ABCMeta , abstractmethod

class programing(metaclass = ABCMeta):  # canot be called or initilze
    @abstractmethod      
    def has_opp(self):
        pass
     
class python(programing):
    def has_opp(self):
        return "Yes"

class pascal(programing):
    def has_opp(self):
        return "NO"

one = python()
print(one.has_opp())



