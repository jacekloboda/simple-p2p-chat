import socket as s
import threading

HOST = "0.0.0.0"


def start_server(port, ready_event):

    with s.socket(s.AF_INET, s.SOCK_STREAM) as socket:

        socket.bind((HOST, port))
        socket.listen()

        print(f"[server] listening on {
              s.gethostbyname(s.gethostname())}:{port}")

        ready_event.set()

        conn, addr = socket.accept()

        print(f"[server] connected to {addr}")

        with conn:

            while True:

                data = conn.recv(1024)
                if not data:
                    break

                print(f"[server] recieved: {data.decode()}")


def start_client(target_ip, target_port, ready_event):

    ready_event.wait()

    with s.socket(s.AF_INET, s.SOCK_STREAM) as socket:

        socket.connect((target_ip, target_port))

        print(f"[client] connected")

        while True:

            message = input("[client] enter message or 'exit' to stop: \n")

            if message.lower() == "exit":
                break

            socket.sendall(message.encode())


if __name__ == "__main__":

    ready_event = threading.Event()
    my_port = int(input("enter your PORT: "))

    server_thread = threading.Thread(
        target=start_server, args=(my_port, ready_event), daemon=True)

    server_thread.start()

    ready_event.wait()

    target_ip = input("enter target IP: ")
    target_port = int(input("enter target PORT: "))

    start_client(target_ip, target_port, ready_event)
