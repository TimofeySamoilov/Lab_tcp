import socket
import random


# parameters:
communication_file = "../communication.txt"
port_start = 65430
port_end = 65440

def handle_client(client_socket):
    while True:
        try:
            # receiving a message from client...
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            match message:
                case "_code1g":
                    # do nothing :)
                    # this section is informative, we can just delete it
                    None

                case "_code2g":
                    file = open(communication_file, "r")
                    data = file.readline()
                    file.close()

                    file = open(communication_file, "w")
                    answer = random.randint(5, 100) * "+"
                    file.write(answer)
                    file.close()
                    print("Get from client:", data)
                    print("Sent to client:", answer)

                    message = "_code3g"
                    client_socket.send(message.encode('utf-8'))

        except ConnectionResetError:
            print("(!) Client disconnected")
            break
        except Exception as e:
            print("(!) Something went wrong:", e)


    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in range(port_start, port_end):
        try:
            server.bind(('localhost', port))
            server.listen(1)
            print("Server listening on port", port)

            client_socket, addr = server.accept()
            print(f"Accepted connection from {addr}")
            handle_client(client_socket)
            break

        except OSError as e:
            match e:
                case OSError():
                    print(f"(!) Port {port} is already in use. Trying next port...")
                case _:
                    print(f"(!) An unexpected error occurred: {e}")





if __name__ == "__main__":
    start_server()
