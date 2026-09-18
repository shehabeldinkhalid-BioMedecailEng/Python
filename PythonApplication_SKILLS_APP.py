import sqlite3 as sql
input_Mess_List = [("s","Show all skills"),("a","Add New Skill"),("d","Delete A Skill"),("u","Update Skill Progress"),("q","Quit The App")] 
print("Welcome to the Skills App")
print("You can do the following:")
for item in input_Mess_List:
    print(f"{item[0]} ====> {item[1]}")
user_choice = input("Please enter your choice:").lower().strip()
while user_choice != "q":

    for item in input_Mess_List:
        if user_choice == item[0]:
            print(item[1])
            comand= item[0]
            break
        elif user_choice != item[0]:
            continue
    if user_choice not in [item[0] for item in input_Mess_List]:
        print("Invalid choice, please try again.")
    # Connect to the SQLite database
    conn = sql.connect('personal_skills.db')
    # Create a cursor object
    cursor = conn.cursor()
    # Create the skills table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS skills(skill_id INTEGER ,skill_Num INTEGER ,Skill TEXT)")
    if comand == "s":
        # Show all skills
        cursor.execute("SELECT * FROM skills")
        rows = cursor.fetchall()
        print("Here are your skills:")
        for row in rows:
            print(f"Skill ID: {row[0]}, Skill Number: {row[1]}, Skill: {row[2]}")
    elif comand == "d":
        skill_id = input("Enter the Skill ID to delete: ")
        row_=cursor.execute(f"SELECT * FROM skills WHERE skill_id = {skill_id}").fetchone()
        print(f"the skill is ===> {row_[2]}")
        ans=input(f"are you sure you want to delete {row_} : use yes or no\n").lower().strip()
        if ans == "yes":
            cursor.execute(f"DELETE FROM skills WHERE skill_id = {skill_id}")
            conn.commit()
            print(f"Skill with ID {skill_id} has been deleted.")
        elif ans == "no":
            print("Skill deletion cancelled.")
        else:
            print("Invalid response. Please enter 'yes' or 'no'.Try again")
    elif comand == "u":
        # Update skill progress
        skill_id = input("Enter the Skill ID to update: ")
        new_skill = input("Enter the new skill name: ")
        cursor.execute(f"UPDATE skills SET Skill = {new_skill} WHERE skill_id = {skill_id}")
        conn.commit()
        print(f"Skill with ID {skill_id} has been updated to {new_skill}.")
    elif comand == "a":
        # Add a new skill
        skill_id = input("Enter the Skill ID: ")
        skill_num = input("Enter the Skill Number: ")
        skill_name = input("Enter the Skill Name: ")
        cursor.execute(f"INSERT INTO skills (skill_id, skill_Num, Skill) VALUES  ({skill_id},{ skill_num},'{skill_name}')",)
        conn.commit()
        print(f"Skill {skill_name} has been added with ID {skill_id} and Number {skill_num}.")
    else:
        print("Invalid command. Please try again.")
    break
print("Thank you.....smile!")