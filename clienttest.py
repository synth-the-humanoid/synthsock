import synthsock

def send(sock):
    print("Message: ",end="")
    msg = input()
    msg += "\n"
    sock.sendall(msg.encode())
    return 0


print("Server to connect to: [default: localhost] ",end="")
server = input()

if server == "":
    server = "localhost"

print("Port to connect to: [default: 10000] ",end="")
port = input()
if port == "":
    port = 10000
if synthsock.client(server, port, send) == -1:
    print("Error in server / port format")

