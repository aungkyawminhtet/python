data = {0: {'u_Email': 'aung', 'u_Password': 'aung', 'u_Name': 'akmh', 'u_Phone': '09999', 'u_Age': '100'}}
u_data = input("Enter something :")
for i in range(len(data)):
    if data[i]["u_Email"] == u_data:
        print("this is already exit.")
    elif data[i]["u_Email"] != u_data:
        data[i]["u_Email"] = u_data
        print(data)
    else:
        print("something wrong")