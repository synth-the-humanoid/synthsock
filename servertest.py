import synthsock

def call(conSock, cliAddr):
    current = ""
    msg = ""
    while(current != "\n"):
        msg += current
        current = conSock.recv(1).decode()

    print("[" + str(cliAddr[0]) + "]: " + msg)
    return 0;

print("Port Number: [default: 10000] ",end="")
port = input()
if port == "":
    port = "10000"
synthsock.server("localhost", port, 1, call)

