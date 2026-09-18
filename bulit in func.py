# =============== App 1 ========================
# Function ==> ( any )
array_OF_any = [0,0]
print(len(array_OF_any))
if any(array_OF_any):
    print("at least one item == > 1 ")
else:
    print("yes all items are == > 0 ")

# Function ==> ( all )
array_OF_all = [1,1,1] 
if all(array_OF_all):
    print("yes all items are == > 1 ")
else:
    print("at least one item == > 0 ")

# =============== App 2 ========================
# Function bin() and id()

# X = input("write number you want to know it's binary code and memory location\n")
# print(bin(int(X)))
# print(id(int(X)))


# Function sum(iterable,start)
list = [1,2,3,4,5]    # 15 
print(sum(list , 1 )) # 16

# Function round( number , numofdigits )
print(round(3.500)) # 4         
print(round(3.400)) # 3
print(round(3.600)) # 4
print(round(3))     # 3

# Function print("str",sep" ") to change defualt separator
print(
      "How" ,
      "are",
      "you",
      sep="|"
      )

print("Hi",end=" ")
print("shehab")
print("new line")

# Function pow( int base {N} , int power {N} , int moduls {NotN})
print(pow(2,3))
print(pow(2,3,3))

# Function min(iterator) and max(iterator) take integer or str
MYlist = [1,2,3,4,5,6,7,8,9,10]
print(min(MYlist))
print(max(MYlist))
print(max("x","X","R"))

# Function slice(start , end , step)
MYlist = ["shehab","eman","amr","mohamed","hassan","belal","sara","aya"]
print(MYlist[slice(2,5)])
print(MYlist[slice(0 , 5 , 2)])

# Function Map( function , iterable )
def function(text):
    Ntext=text.lower().capitalize().strip()
    return f"== {Ntext} =="

mytexts =[" shehab ","Hana ","  baSent "," REAm"] 
print(map(function,mytexts))
for Name in map(function,mytexts):
    print(Name)
#=================== Same app W.D.N.of.lines ===============================================
for Name_2 in map(lambda Namy : f"Hi {Namy.lower().capitalize().strip()}",mytexts):
    print(Name_2)


# Function filter( function , iterable ) --> return only true boolen
# ex 1
mynums = [1,2,3,4,5,6,8,7,8,9,10]
def checknum(num):
    if num > 3:
        return True
for i in filter(checknum,mynums):
    print(i) 
 
# ex 2    
H = input("letter\n") 
Names = ["Shehab","Sara","Hana","Islam","Sona","Sandy","Ream"]
def checkname(iterator,index = 0):
    for i in range(len(Names)) :
        if iterator[i][index].lower() == H.lower():
            return True
        else:
            return False

for X in filter(checkname,Names):
    print(f"== {X} ==\n")

# ======================== another way ======================================
Names = ["Shehab","Sara","Hana","Islam","Sona","Sandy","Ream"]
H = input("letter\n").lower().strip() 
def checknames(name):
    Nname=name.lower().strip() 
    return Nname.startswith(H)

for i in filter(checknames,Names):
    print(f"== {i} ==\n")

# ex 3
Names = ["Shehab","Sara","Hana","Islam","Sona","Sandy","Ream"]
H = input("letter\n").upper().strip() 
for i in filter(lambda Nname : Nname.startswith(H) , Names):
    print(f"== {i} ==\n")



# Function reduce( function , iterable ) --> recertion
from functools import reduce
mynums = [1,2,3,4,5,6,7,8,9,10]   # 55
def FUN( num1 , num2  ):
    return num1 + num2  
print(reduce(FUN,mynums))


# Function enumerate( iterable , start = 0 ) --> counter
Myskills = ["shehab","khalied","mohamed","roqa","ibrahem","hi"]
X = enumerate(Myskills,1)
print(type(X))
for skill in X:
    print(skill)

# help(function) and reversed(iterable)
print(help(print))
list= ["shehab","khalied","mohamed","roqa","ibrahem"]
for i in (reversed(list)):
    print(i)
        

# zip( N-iterables  ) 
A_1 = [1,2,3,4,5]
A_2 = ["A","B","C"]
ultimateA = zip( A_1 , A_2 ) 
print(ultimateA)
for item in ultimateA:
    print(item)
    
tupel = ("Man","Women","Dog","Cat","Sun","Star")
Dic1 = {"Name":"shehab","Work":"Eng","age":19}
for X , Y , M , T in zip(A_1 , A_2,tupel,Dic1):
    print(f"List 1 ==> {X} List 2 ==> {Y} List 3 ==> {M} List 4 ==> {T} ==> {Dic1[T]}")
    
