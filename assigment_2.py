#Aung Kyaw Min htet Assigment II
import ast
db = {}
global email_exit
email_exit = -1

def main_sector():
    main_option = int(input("Press 1 to Registration \nPress 2 to Login \nPress 3 to exit: "))
    if main_option == 1:
        registration()
    elif main_option == 2:
        login()
    elif main_option == 3:
        exit(1)
    else:
        print("Inalid option")
        main_sector()


def registration():
    user_email = input("Enter your Registration Email:")
    user_get = email_exit(user_email)
    if user_get != None:
        print("Email is already Exit.")
        registration()
    else:
        user_Passowrd = input("Enter your Registration Password:")
        user_Name = input("Enter your Username:")
        user_Phone = int(input("Enter your Phone Number:"))
        user_Age = int(input("Enter your Age:"))

        id = len(db)

        to_insert = {id:{"u_Name" : user_Name , "Email" : user_email , "Password" : user_Passowrd , "u_Phone" : user_Phone , "u_Age" : user_Age}}
        db.update(to_insert)


def login():
    user_found = -1
    print("This is login Sector")

    l_user_email = input("Enter your login Eamil:")
    l_user_password = input("Enter your login password:")

    for i in range(len(db)):
        if db[i]["Email"] == l_user_email and db[i]["Password"] == l_user_password:
            user_found = i
    if user_found != -1:
        print("Login Success")
        profile(user_found)
    else:
        print("Invalid Nod Found")


def profile(info):
    print("Welcome ", info)
    print("User detail is ",db[info]["Email"])

    exit_code = int(input("Press 1 to exit and record data!:"))
    if exit_code == 1:
        record_all_data()

    

def email_exit(email):
    length = len(db)
    for i in range(length):
        if db[i]["Email"] == email:
            return i
        

def record_all_data():
    with open("note.txt",'a') as file:
        file.writelines(str(db))

def loading_all_data():
    with open("note.txt",'r') as f:
        re_use = f.read()
        data= ast.literal_eval(re_use)
        db.update(data)
        

if __name__ == '__main__':
    loading_all_data()    
    print(db)
    while True:  
         main_sector()
     
    
