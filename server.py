import os
import socket
from http import HTTPStatus
from helper import get_open_port


def body_fun(list_of_data, add):
    method = list_of_data[0].split()[0]
    try:
        status = int(list_of_data[0].split()[1][9:])
        phrase = HTTPStatus(status).phrase
    except ValueError:
        status = 200
        phrase = HTTPStatus(status).phrase
    headers = '\n'.join(i for i in list_of_data[2:])
    body = f"<pre>Request method: {method}<pre>" \
           f"<pre>Request source: {add}</pre>" \
           f"<pre>Request status: {status} {phrase}</pre>" \
           f"<pre>{headers}</pre>"
    print(headers)
    return body


def headers_fun():
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html; charset=UTF-8'
    ])
    return headers


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
                text = conn.recv(1024).decode('utf-8')

                print(f'Received:\n\n {text} \n\n')

                response = '\r\n\r\n'.join([
                    headers_fun(),
                    body_fun(text.split("\n"), r_address)
                ])

                if text:
                    print("Sending data back to the client")
                    conn.send(response.encode('utf-8'))
                else:
                    print(f"No data from {r_address}")
                    break
            conn.close()


if __name__ == "__main__":
    main()
