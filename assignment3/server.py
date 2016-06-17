#!/usr/bin/env python          

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12348                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting\n')
   
   msg='hi'
  

   while(msg!='bye'):
     print('enter the message')
     msg=raw_input() 
     c.send('server:'+msg)
     print c.recv(1024)
   c.close()                # Close the connection
   s.close()
