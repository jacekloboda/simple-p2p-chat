import socket as s

HOST = "0.0.0.0"
PORT = 12345


def start_server():

    with s.socket(s.AF_INET, s.SOCK_STREAM) as socket:

        socket.bind((HOST, PORT))
        socket.listen()
        print(f"listening on {HOST}:{PORT}")

        conn, addr = socket.accept()

        with conn:

            print(f"connected to {addr}")

            while True:

                data = conn.recv(1024)
                if not data:
                    break

                print(f"recieved: {data.decode()}")
                conn.sendall(data)


if __name__ == "__main__":
    start_server()
