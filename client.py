import socket as s

HOST = "0.0.0.0"
PORT = 12345


def start_client():

    with s.socket(s.AF_INET, s.SOCK_STREAM) as socket:

        socket.connect((HOST, PORT))

        while True:

            message = input("enter message or 'exit' to stop: ")

            if message.lower() == "exit":
                break

            socket.sendall(message.encode())
            data = socket.recv(1024)

            print(f"recieved: {data.decode()}")


if __name__ == "__main__":
    start_client()
