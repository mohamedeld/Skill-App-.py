# import sqlite3
import sqlite3

# connect database
db = sqlite3.connect("appp.db")

# setting up for cursor
cr = db.cursor()


# function commit and close
def commit_and_close():
    db.commit()  # save (commit) changes
    db.close()  # close database
    print("Connection to database is closed")


uid = 1

input_message = """
What Do You Want To Do
"s" => Show All The Skill
"a" => Add New Skill
"d" => Delete a Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option
"""
# input option chosen
user_input = input(input_message).strip().lower()

# command list
command_list = ["s", "a", "d", "u", "q"]


# Define the method
def show_skills():
    cr.execute(f"select * from skills where user_id = '{uid}'")
    result = cr.fetchall()
    print(f"You Have {len(result)} Skills")
    for row in result:
        print(f"Skill => {row[0]}", end=" ")
        print(f"Progress => {row[1]}%")

    commit_and_close()


def add_skill():
    skill_name = input("Enter Skill Name").strip().capitalize()

    cr.execute(f"select name from skills where name = '{skill_name}' and user_id = '{uid}'")
    result = cr.fetchone()
    print(f"{result}")

    if result is None:  # there is no skill with this name
        skill_progress = input("Enter Progress Name").strip()

        cr.execute(f"insert into skills(name, progress,user_id) values('{skill_name}','{skill_progress}','{uid}')")

    else:  # there is skill found in database like this name
        print("This Skill Is Exists")

    commit_and_close()


def delete_skill():
    skill_name = input("Enter Skill Name").strip().capitalize()
    cr.execute(f"delete from skills where name = '{skill_name}' and user_id = '{uid}'")
    commit_and_close()


def update_skills():
    skill_name = input("Enter Skill Name").strip().capitalize()
    skill_progress = input("Enter The New Progress Name").strip()

    cr.execute(f"update skills set progress = '{skill_progress}' where name = '{skill_name}' and user_id = '{uid}'")

    commit_and_close()


def quit_skills():
    print("quit skills")

    commit_and_close()


if user_input in command_list:

    # print(f"you chosen is found {user_input}")

    if user_input == "s":

        show_skills()

    elif user_input == "a":

        add_skill()

    elif user_input == "d":

        delete_skill()

    elif user_input == "u":

        update_skills()

    else:
        print("App Is Closed")
        commit_and_close()

else:

    print(f"your chosen \"{user_input}\" not found")
