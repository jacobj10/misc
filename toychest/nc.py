import socket

#create an INET, STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#now connect to the web server on port 80
# - the normal http port
s.connect(("shell2017.picoctf.com", 44840))
while True:
	x = s.recv(1024)
	print x
	line =  x.split('\n')[1]
	parse = line.split("'")
	first = parse[1]
	second = parse[3]
	third = parse[5]
	send_string = ""
	for i in range(int(second)):
		send_string += first
	send_string += third
	s.send(send_string + '\n')
