import json
import socket


class TCPclient:
    def __init__(self, sms):
        self.client_ip = "localhost"
        self.client_port = 6565

        self.input_checking(sms)

    def run_client(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.client_ip, self.client_port))

        return client  # to send and receive data

    def input_checking(self, input_sms):

        if input_sms == "reg":
            self.registor(input_sms)
        elif input_sms == "login":
            self.client_login(input_sms)
        elif input_sms == "gad":
            self.get_all_data(input_sms)
        else:
            print("Invalid Option!")

    def get_all_data(self, sms):
        client = self.run_client()

        # send data to server
        send_sms = bytes(sms, 'utf-8')
        client.send(send_sms)

        # received data from server
        recv_from_server = client.recv(4029)
        # print(recv_from_server.decode('utf-8'))
        dict_data: dict = json.loads(recv_from_server.decode('utf-8'))
        print(type(dict_data))
        print(dict_data)
        client.close()

    def registor(self, info):
        print("#####---This is Registor Section!---#####")

        client = self.run_client()
        try:
            r_name = input("Enter your registor name :")
            r_email = input("Enter your registor email :")
            r_password = input("Enter your registor password :")
            r_data = info + ' ' + r_email + ' ' + r_password + ' ' + r_name
            send_r_data = bytes(r_data, 'utf-8')
            client.send(send_r_data)

            recv_from_server = client.recv(2049)
            print(recv_from_server.decode('utf-8'))

        except Exception as err:
            print(err)

    def client_login(self, info):
        print("#####---This is Login Section.---#####")
        try:
            l_email = input("Enter your email to login:")
            l_password = input("Enter your login password:")
            client = self.run_client()
            send_sms = info + ' ' + l_email + ' ' + l_password
            l_send_sms = bytes(send_sms, 'utf-8')
            client.send(l_send_sms)
            recv_from_server = client.recv(4029)
            print(recv_from_server.decode('utf-8'))
            client.close()

        except Exception as err:
            print(err)


if __name__ == '__main__':
    while True:
        print("#####---This is only comment reg, login, gad---#####")
        sms: str = input("Enter your comment : ")
        run_client = TCPclient(sms)
