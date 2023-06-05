#Assigment V
#Aung Kyaw Min Htet
import socket
import pymongo
#import subprocess

class TCPserver:
    def __init__(self):
        self.server_ip = "localhost"
        self.server_port = 9997
        self.connection = pymongo.MongoClient("localhost", 27017)
        self.datadb = self.connection["akmh"]
        self.collector = self.datadb["admin"]

    def main_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen()
        print(("Server is Listening."))
        try:
            while True:
                client, address = server.accept()
                print("Conneted from client {} and {}".format(address[0], address[1]))
                self.handle_client(client)
        except Exception as err:
            print(err)

    def handle_client(self, client):
        with client as sock:
            from_client = sock.recv(1024)
            recv_data = from_client.decode('utf-8')

            # print("Running Command :", recv_data)
            try:
                # return_data = subprocess.call(recv_data , shell=True)
                cmd_data = recv_data.lower()
                if cmd_data == "gad":  #gad is get all data
                    print("*******Get all data from mongo database********")
                    for i in self.collector.find():
                        print(i)

                # print(("***********\n", return_data))
                # print("###################")

            except Exception as err:
                print(err)

            message = "Server got that :>" + recv_data
            to_send = bytes(message, 'utf-8')
            sock.send(to_send)
            print("Receive from client :", from_client)


if __name__ == '__main__':
    t_server = TCPserver()
    t_server.main_server()
