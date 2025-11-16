import socket
import sys

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
BUFSIZE = 1024


if  len(sys.argv) < 2:
  print("no port specyfied, using 8000")
  port=8000
else:
  port = int( sys.argv[1] )

print("Will listen on ", HOST, ":", port)


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
  s.bind((HOST, port))

  while True:
    data_address = s.recvfrom( BUFSIZE )
    data = data_address[0]
    address = data_address[1]
    print( "Message from Client:{}".format(data) ) 
    print( "Client IP Address:{}".format(address) ) 

    if not data:
      print("Error in datagram?")  
      break

    response = str(len(data)).encode()
    s.sendto(response, address )
    print(f'Sending number of bytes recieved ({len(data)})')
