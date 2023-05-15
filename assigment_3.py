#Assigment III
#Aung Kyaw Min Htet

db = {} #this is database

def main_sector():

    main_option = input("Press 1 to Registor \nPress 2 to LogIn \nPress 3 to Exit:")

    try:
        update_option = int(main_option)
    except ValueError:
        update_option = str(main_option)
        print("Please only enter integer number!")
        main_sector()

    if update_option == 1:
        registion_section()
    elif update_option == 2:
        login_section()
    elif update_option == 3:
        recording_all_data()
        exit(1)
    else:
        print("Invlid Option!")
        update_option()

def registion_section():

    print("This is registion Section--!.")
    user_Email = input("Please enter registion Email:")

    email_get = email_exit(user_Email)
    if email_get != None:
        print("Email is already Exit!")
        print("Please enter another email!")
        login_section()
    else:
        user_Password = input("Please enter registion Password:")
        user_Name = input("Please enter Username:")
        user_Phone = int(input("Please enter Phone Number:"))
        user_Age = int(input("Please enter Age:"))

        id = len(db)

        to_insert = {id:{"u_Email" : user_Email , "u_Password" : user_Password , "u_Name" : user_Name , "u_Phone" : user_Phone , "u_Age" : user_Age}}
        db.update(to_insert)


def login_section():
    user_found = -1

    print("This is Login Section--!.")

    l_user_email = input("Please enter login Email:")
    l_user_password = input("Please enter login Password:")

    for i in range(len(db)):
        if db[i]["u_Email"] == l_user_email and db[i]["u_Password"] == l_user_password:
            user_found = i
    if user_found !=-1:
        print("Login Success")
        user_profile(user_found)
    else:
        print("Account Not Found!")

def email_exit(email):
    length = len(db)
    for i in range(length):
        if db[i]["u_Email"] == email:
            return i

def user_profile(user_found):
    print("Welcome",db[user_found]["u_Email"])

    option = int(input("Press 1 to recording all data \npress 2 to Update data :"))
    if option == 1:
        recording_all_data()
    elif option == 2:
        update_Data()
    else:
        print("Please enter 1 and 2 !!")

def recording_all_data():
    with open("note.txt" , 'w') as file:
        for i in range(len(db)):
            email = db[i]["u_Email"]
            password = db[i]["u_Password"]
            name = db[i]["u_Name"]
            phone = db[i]["u_Phone"]
            age = db[i]["u_Age"]
            total_all_data = email + ' ' + password + ' ' + name + ' ' + str(phone) + ' ' + str(age) + ' '
            file.write(total_all_data)
    print("----Data is all recorded!----")

def loading_all_data():
    with open("note.txt" , 'r') as datas:
        re_use = datas.readlines()
        for data in re_use:
            re_use_data = data.split(" ")

            id = len(db)
            data_loading = {id : {"u_Email" : re_use_data[0] , "u_Password" : re_use_data[1] , "u_Name" : re_use_data[2] , "u_Phone" : re_use_data[3] , "u_Age" : re_use_data[4]}}
            db.update(data_loading)
        

#Update data function
def update_Data():
    print("-----This is data update Section-----")
    print("Press 1 to Email update\nPress 2 to password update\nPress 3 to username update\nPress 4 to Phone update\nPress 5 to Age update")
    user_option = int(input("Please choice update number :"))
    user_update = input("Please enter update data :")

    try:
        u_update = str(user_update)
    except ValueError:
        u_update = int(user_update)

    if user_option == 1:
        for i in range(len(db)):
            if db[i]["u_Email"] == u_update:
                print("Already Exit!")
                update_Data()

            elif db[i]["u_Email"] != u_update:
                db[i]["u_Email"] = u_update
                print("Email updated :", db)
            else:
                print("Invaild Option!")
                update_Data()

    if user_option == 2:
        for i in range(len(db)):
            db[i]["u_Password"] = u_update
            print("Password updated:", db)

    if user_option == 3:
        for i in range(len(db)):
            db[i]["u_Name"] = u_update
            print("Name updated:", db)

    if user_option == 4:
        for i in range(len(db)):
            db[i]["u_Phone"] = u_update
            print("Phone updated:", db)

    if user_option == 5:
        for i in range(len(db)):
            db[i]["u_Age"] = u_update
            print("Age updated :", db)

if '__main__' == __name__:
    loading_all_data()
    print(db)
    while True:
        main_sector()
