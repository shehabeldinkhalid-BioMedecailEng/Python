def shehab():
    print("Hi shehab")
    return "shehab"

# APP_1
# filter(lambda name : f ,iterator)
H = "s" 
Names = ["Shehab","Sara","Hana","Islam","Sona","Sandy","Ream"]
for X in range(0,len(Names)):
    if Names[X][0].lower() == H.lower():
        print(f"{Names[X]}")

# open and close file app
EE = False
ET = True
right_pass = "Shehab"
counter = 3
while counter != 0 and (EE==False and ET == True):
        ans1 = input("Please Enter Password\n").strip().lower().capitalize()
        if ans1 == right_pass:
            while (EE==False and ET == True):
                ans2=input(f"""
                    Enter Mood
                    Choose Number from one to three 
                    1- [read] ==> read what's inside the File
                    2- [write] ==> rewrite what's inside the File
                    3- [both] ==> able make [1] , [2]
                    \n
                    """).strip().lower()   
                try: 
                    ans2=int(ans2)
                except:
                    continue
                else:
                    try:
                        ans2<4
                        ET = False
                    except:
                        raise ValueError("You have only [1]-[2]-[3] choose from them invalied NUM")
                    else:
                        EE=True
        else:
            counter-=1
            continue
            
if counter == 0:
    print("Sorry your password is wrong")
else:
    if ans2 == 1:
        print(f"Your file is open on Mood Read ") 
        File=open(r"C:\Users\SHIBA_LION\Desktop\my books\python\python projects\__pycache__\saved.txt","r")
    elif ans2 == 2:
        print(f"Your file is open on Mood Write ") 
        File=open(r"C:\Users\SHIBA_LION\Desktop\my books\python\python projects\__pycache__\saved.txt","w")
    elif ans2 == 3:
        print(f"Your file is open on Mood both ") 
        File=open(r"C:\Users\SHIBA_LION\Desktop\my books\python\python projects\__pycache__","r+")
    else:
        raise ValueError("You have only [1]-[2]-[3] choose from them invalied NUM")
Close=input("Do you want to close the File Yes or No\n").strip().lower()
if Close == "yes":
    File.close()
    print("Your File is closed")
else:
    print("Ok your file still opened")

    