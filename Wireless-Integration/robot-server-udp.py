# In order to stop the server, in the terminal press CTRL+C and then on the app press disconnect

import socket
from convertToTwist import convertToTwist



# Function declaration
def convertToTwist(data):
    if data == 'Stop\n':
        x = 0
        y = 0
        z = 0
        th = 0
    else:    
        x = moveBindings[data][0]
        y = moveBindings[data][1]
        z = moveBindings[data][2]
        th = moveBindings[data][3]

    # TODO this is just for programming
    print('x = ', x, ', ' , 'y = ', y, ', ', 'y = ', z, ', ', 'th = ', th, '\n')

    #TODO convert to twist object


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
print ("Socket successfully created")
port = 8001
s.bind(('', port))
print ("Socket binded to %s" %(port))
s.listen(1)
print ("Socket is listening... Press the Connect button on the android app")


while True:
    c, addr = s.accept()
    print ('Got connection from', addr )
    c.send('Thank you for connecting\n'.encode('utf-8'))
    while True:
        try:
            data =c.recv(1024)
            data =data.decode('utf8')
            print('Command sent:', data)
            convertToTwist(data)
            if not data:
                print("Disconnected from ", addr)
                break

        except KeyboardInterrupt:
            print("keyboard interrupted")
            s.close()
            exit()
        except Exception as error:
            print("Failed to insert record into Laptop table {}".format(error))
            exit()
                                                                                  
