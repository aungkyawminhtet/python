#Aung Kyaw Min Htet
#Assigment VI
#Registation in server and to save mongo database

import json
import socket
import pymongo
import random

class TCPserver:
    def __init__(self):
        self.server_ip = "localhost"
        self.server_port = 6565

        #This is from mongo database
        self.connection = pymongo.MongoClient("localhost", 27017)
        self.database = self.connection["akmh"]
        self.collector = self.database["admin"]

    def main_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen()
        print("server is listening.")
        try:
            while True:
                client, address = server.accept()
                print("Connect from client ip - {} and port - {}.".format(address[0], address[1]))
                self.handle_client(client)
        except Exception as err:
            print(err)

    def handle_client(self, sock_client):

        with sock_client as sock:
            data_list = [] #to accept from client input data
            recv_sms = sock.recv(1024)
            data_list = recv_sms.decode('utf-8').split(' ')
            # print(data_list)

            if data_list[0] == "reg":
                self.server_registor(sock, data_list)
            elif data_list[0] == "login":
                self.server_login(sock, data_list)
            elif data_list[0] == "gad":
                self.get_all_data(sock)
            else:
                sms = bytes("Invalid Opton!", 'utf-8')
                sock.send(sms)

    def get_all_data(self, sock):
        data_collector: dict = {}
        for i in self.collector.find({}, {"_id": 0, "name": 1, "email": 1, "password": 1}):
            id = len(data_collector)
            db = {id: {"name": i["name"], "email": i["email"], "password": i["password"]}}
            data_collector.update(db)
        str_data = json.dumps(data_collector)
        print(type(str_data))
        print(str_data)

        send_str_data = bytes(str_data, 'utf-8')
        sock.send(send_str_data)
        print("Tips - Client use gad function.")

    def server_registor(self, sock, data_list):
        get_email = self.email_checking(data_list)
        print("get_email is :",get_email)

        if get_email is not None:
            sms_send = "Email is already exit!.\nPlease enter another email!"
            sock.send(bytes(sms_send, 'utf-8'))

        else:
            r_id = random.randint(100, 10000)
            server_email = data_list[1]
            server_password = data_list[2]
            server_name = data_list[3]
            reg_data = {"_id": r_id, "name": server_name, "email": server_email, "password": server_password}
            insert_data = self.collector.insert_one(reg_data)
            sock.send(bytes("Register data is update", 'utf-8'))
            print(insert_data)

    def email_checking(self, data_list):
        check_email = data_list[1]
        for i in self.collector.find({}, {"_id": 0, "email": 1}):
            if check_email == i["email"]:
                return i

    def server_login(self, sock, data_list):
        server_email = data_list[1]
        server_password = data_list[2]
        flag = -1
        for i in self.collector.find({}, {"_id": 0, "email": 1, "password": 1}):
            if server_email == i["email"] and server_password == i["password"]:
                flag = 1
                break
            # else:
            #     sock.send(bytes("Account Not Found!", 'utf-8'))
            #     break

        if flag == 1:
            data = bytes("Login Success!", 'utf-8')
            sock.send(data)
        else:
            data = bytes("Email and Pssword are Incorrect!", 'utf-8')
            sock.send(data)



if __name__ == '__main__':
    server_connect = TCPserver()
    server_connect.main_server()

