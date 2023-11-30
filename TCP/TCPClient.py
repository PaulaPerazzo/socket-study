from socket import *

server_name = "150.161.1.101"
server_port = 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
sentence = input("input a lower case sentence: ")
client_socket.send(sentence.encode())
modified_sentence = client_socket.recv(1024)
print("from server: ", modified_sentence)
client_socket.close()
