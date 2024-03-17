import zmq
import socket

# setting the subscribe of ZeroMQ
context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:55556")  # change to your own ZeroMQ address
subscriber.setsockopt_string(zmq.SUBSCRIBE, '')  # subscribe all notifications 

# setting the UDP for Wireshark 
udp_ip = "127.0.0.1"
udp_port = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = subscriber.recv()
    sock.sendto(message, (udp_ip, udp_port))
