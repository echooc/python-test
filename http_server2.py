import socket
server = '218.87.136.6'
PORT = 80
BUFLEN = 1024

class connect():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print 'socket created'
        try:
            s.connect((server, PORT))
            print 'socket connected to www.jxust.edu.cn'
            rstr = s.recv(BUFLEN)
            print 'received>>>>>>>', rstr
        except socket.error, e:
            print e
        message = 'GET / HTTP/1.1\r\n\r\n'

        try:
            s.sendall(message)
        except socket.error, e:
            print e
        print 'message send successfully!'

        reply = s.recv(BUFLEN)
        print reply

        s.close()

if __name__ == '__main__':
    cn = connect()

