import socket
class TCPclient:
    def __init__(self, sms):
        self.target_ip = "localhost"
        self.target_port = 9997


        self.send_and_recv_data = {}
        self.client_sms = bytes(sms, 'utf-8')
        self.send_and_recv_data.update({len(self.send_and_recv_data): self.client_sms})

    def main(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))
        client.send(self.client_sms)

        from_server = client.recv(4096)
        recv_sms = from_server.decode('utf-8')
        self.send_and_recv_data.update({len(self.send_and_recv_data) : recv_sms})
        print("Receive sms from server :", recv_sms)
        print(self.send_and_recv_data)


if __name__ == '__main__':
    while True:
        sms: str = input("Enter send message :")
        c_client = TCPclient(sms)
        c_client.main()
