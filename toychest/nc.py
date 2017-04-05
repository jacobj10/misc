import socket

#create an INET, STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#now connect to the web server on port 80
# - the normal http port
s.connect(("shell2017.picoctf.com", 7908))
while True:
	x = s.recv(1024)
	if "flagperson" in x:
		print x

