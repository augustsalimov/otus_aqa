import os
import socket
from http import HTTPStatus
from helper import get_open_port


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        srv_address = ('', get_open_port())
        print(f"\nStarting on {srv_address}, pid: {os.getpid()}")

        sock.bind(srv_address)
        sock.listen(1)

        while True:
            print("Waiting for a connection...")
            conn, r_address = sock.accept()

            print("\nConnection from", r_address)
            while True:
                received_text = conn.recv(1024).decode('utf-8')

                print(f'Received:\n\n {received_text} \n\n')

                # forming body
                list_of_received_text = received_text.split("\n")
                method = list_of_received_text[0].split()[0]
                try:
                    status = int(list_of_received_text[0].split()[1][9:])
                    phrase = HTTPStatus(status).phrase
                except ValueError:
                    status = 200
                    phrase = HTTPStatus(status).phrase
                received_headers = '\n'.join(i for i in list_of_received_text[2:])
                body = f"<pre>Request method: {method}<pre>" \
                       f"<pre>Request source: {r_address}</pre>" \
                       f"<pre>Request status: {status} {phrase}</pre>" \
                       f"<pre>{received_headers}</pre>"

                # forming headers
                headers = '\r\n'.join([
                    f"HTTP/1.1 {status} {phrase}",
                    "Content-Type: text/html; charset=UTF-8",
                    f"Content-Length: {len(body.encode('utf-8'))}"
                ])

                # sum
                response = '\r\n\r\n'.join([
                    headers,
                    body
                ])

                if received_text:
                    print("Sending data back to the client")
                    conn.send(response.encode('utf-8'))
                else:
                    print(f"No data from {r_address}")
                    break
            conn.close()


if __name__ == "__main__":
    main()
