# In order to stop the server, in the terminal press CTRL+C and then on the app press disconnect

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s = socket.socket()         
print ("Socket successfully created")
port = 8001
s.bind(('', port))
print ("socket binded to %s" %(port))
s.listen(1)
print ("socket is listening")
while True:
    c, addr = s.accept()
    print ('Got connection from', addr )
    c.send('Thank you for connecting\n'.encode('utf-8'))
    while True:
        try:
            data =c.recv(1024)
            data =data.decode('utf8')
            print(data)
            if not data:
                print("Disconnected from ", addr)
                break

        except KeyboardInterrupt:
            print("keyboard interrupted")
            s.close()
            exit()
        except Exception as error:
            print("Failed to insert record into Laptop table {}".format(error))
                                                                                  
