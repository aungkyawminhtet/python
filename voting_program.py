##Voting Program for Assigment IV
##Aung Kyaw Min Htet 

class Voting:
    def __init__(self):
        print("This is Voting Program for Assigment 4!")

        self.voter_list = {0 :{"name" : "Rooney" , "v_mark" : 0 ,"voter" : []},
                           1 :{"name" : "Ronaldo" , "v_mark" : 0 , "voter" : []},
                           2 :{"name" : "Messi" , "v_mark" : 0 , "voter" : []},
                           3 :{"name" : "Naymer" , "v_mark" : 0 , "voter" : []},
                           4 :{"name" : "akmh" , "v_mark" : 0 , "voter" : []}}

        self.db: dict = {}
        self.id: int = 0
        self.l_id: int = 0
        self.s_money: int =0
        self.u_money: int=0

    def main_section(self):   #main Section
        print("Loading data :",self.db)
        print("#######This is Main Section.######")
        try:
            main_option = int(input("Press 1 to Registor\nPress 2 to Login\nPress 3 to Exit :"))
        except Exception as err:
            print("Please Enter only integer 1,2,3!")

        if main_option == 1:
              self.registor()
        elif main_option == 2:
            self.login()
        elif main_option == 3:
            exit(1)
        else:
            print("Invalid Option!")
            self.main_section()

    def registor(self):   #Registation Section
    
        print("#####--This is Registor Section--####")
        pass_match = False

        try:
            r_email = input("Enter your Registor eamil :")
            r_name = input("Enter your Registor Name :")
            r_phone = input("Enter your Registor Phone Number :")
            r_address = input("Enter your Address :")
            self.s_money = int(input("Enter your Show Money at least 500$ :"))
            
            while pass_match is False:
                r_pass = input("Enter your Registor Password :")
                c_pass = input("Enter your Comfirm Password :")

                if r_pass != c_pass:
                    print("Password was not Match!\nTry Again!")

                else:
                    print("comfirmed password")
                    
                    self.id = len(self.db)
                    data_insert = {self.id : { "email" : r_email , "username" : r_name ,"phone" : r_phone , "address" : r_address , "password" : c_pass , "point" : self.s_money }}
                    self.db.update(data_insert)
                    print(self.db)
                    
                    pass_match = True

        except Exception as err:
            print("Invalid user Input! Try Again Sir!")
            self.registor()
        
        r_option = False
        while r_option is False:
            try:
                select_option = int(input("Press 1 to Login. \nPress 2 to Main Section. \nPress 3 to Exit :"))

                if select_option == 1:
                    self.login()
                    break

                elif select_option == 2:
                    self.main_section() 
                    break

                elif select_option == 3:
                    exit(1)

                else:
                    print("Invalid Input! Read Againg Option.")

            except Exception as err:
                print("Invalid Option!" , err)
        
    def login(self): #Login Section
        print("#####--This is Login Section--#####")
        l_length = len(self.db)
        
        try:
            for i in range(l_length):
                l_email = input("Enter your Login Eamil :")
                l_password = input("Enter your Login Password :")

                self.l_id = -1
                if l_email == self.db[i]["email"] and l_password == self.db[i]["password"]:
                    self.l_id = i
                    break

            if self.l_id != -1:
                print("Login Success! Welcome :",self.db[self.l_id]["username"])
                self.point()
                #self.user_section(self.l_id)
            else:
                print("Email and Password are Incorrect!")
                self.login()
        except Exception as err:
            print(err,"\n Please enter correct email and password!")


    def point(self):    #point Section
        print("#####--This is point change Section--#####")
        try:
            self.s_money = int(self.db[self.l_id]["point"])
        except Exception as err:
            print(err)

        print("Your money is :",self.s_money)
        print("Point value is 1 pt 500$.")
        ans = input("Do you want to change point ?(y/n) :").lower()
        if ans == 'y':
            r_money = self.s_money/500
            self.u_money = round(r_money)
            print("You have Voting point is :",self.u_money)
            self.user_section(self.l_id)
        else:
            print("You don't have voting point!")


    def user_section(self, l_id):      #user voting section
        #print("Welcom :",self.db[l_id]["username"])

        for i in range(len(self.voter_list)):
            print("Id - {}. Name - {}. Current vote mark - {}".format(i,self.voter_list[i]["name"],self.voter_list[i]["v_mark"]))

        try:
            i_id = int(input("Just enter to Id number to vote :"))#i=input id
            #print(v_id)

            for i in range(len(self.voter_list)):
                if i_id == i:
                    v_id = i_id   

                    self.u_money -=1 #point reduce

                    self.voter_list[v_id]["v_mark"] +=1
                    print(self.voter_list[v_id]["v_mark"])

                    self.voter_list[v_id]["voter"].append(self.db[l_id]["username"])
                    print(self.voter_list[v_id]["voter"])

                    print("Congratulation You are Voted!")
                    print("{} is vote mark is {}".format(self.voter_list[v_id]["name"],self.voter_list[v_id]["v_mark"]))

                    for i in range(len(self.voter_list[v_id]["voter"])):
                        print("Voter :",self.voter_list[v_id]["voter"][i])
                        #print(self.voter_list)

                    print("Your voting point Reaming is :",self.u_money)
                    
                    if self.u_money <=0:
                        print("Try More! You don't have Not enough voting point!")

                        p_option = int(input("Press 1 to Main Section\nPress 2 to Record and Exit :")) #p =point option

                        if p_option == 1:
                            self.main_section()
                        elif p_option == 2:
                            self.recording_all_data()
                            exit(1)
                        else:
                            print("Invalid point option!")

        except Exception as err:
            print(err)

        while True:
            try:
                v_option = int(input("Press 1 to vote again\nPress 2 to Main Section\nPress 3 to Record all data\nPress 4 to Exit :"))
                if v_option == 1:
                    self.user_section(l_id)

                elif v_option == 2:
                    self.main_section()

                elif v_option == 3:
                    self.recording_all_data()
                    exit(1)

                elif v_option == 4:
                    exit(1)

                else:
                    print("Invalid Input!")

            except Exception as err:
                print(err)

    def recording_all_data(self):          #data recording function
        with open("data.txt", 'w') as file:
            for i in range(len(self.db)):
                u_email = self.db[i]["email"] #u=update
                u_name = self.db[i]["username"]
                u_phone = self.db[i]["phone"]
                u_address = self.db[i]["address"]
                u_password = self.db[i]["password"]
                u_point = self.db[i]["point"]
                total_all_data = u_email + ' ' + u_name + ' ' + str(u_phone)+ ' ' + u_address + ' ' + u_password + ' ' + u_point + ' '
                file.writelines(total_all_data)


            for li in range(len(self.voter_list)):
                vu_name = self.voter_list[li]["name"] #vu=voter update
                vu_mark = self.voter_list[li]["v_mark"]
                v_voter = self.voter_list[li]["voter"]

                for i in range(len(v_voter)):
                    vu_voter = self.voter_list[li]["voter"][i]
                    break

                total_vu_all_data = vu_name + ' ' + str(vu_mark) + ' ' + vu_voter 

                file.writelines(total_vu_all_data)

        print("#####--Data all Recorded--#####")

    def loading_data(self):      #data Loading function
        with open("data.txt" , mode='r') as r_file:
            re_use = r_file.readlines()
            for data in re_use:
                re_use_data = data.split(" ")

                loading_id = len(self.db)
                data_loading = { loading_id : {"email" : re_use_data[0] , "username" : re_use_data[1] , "phone" : re_use_data[2] , "address" : re_use_data[3] , "password" : re_use_data[4] , "point" : re_use_data[5]}}

                self.db.update(data_loading)

if __name__ == '__main__':
    voting = Voting()
    voting.loading_data()
    voting.main_section()