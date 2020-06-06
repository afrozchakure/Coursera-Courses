# Making a connection in Python requires 3 lines of code
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()  # Convert the request to UTF-8
mysock.send(cmd)  # We need to send data to server (It sends bytes)

while True:  # It pulls 512 characters at a time
    data = mysock.recv(512) # Get upto 512 characters
    if (len(data) < 1):  # If length of data is less than 1 break
        break
    print(data.decode())  # It converts the UTF-8 data to Unicode
mysock.close()  # Close the socket and release the resource

