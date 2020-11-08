import zmq

#ZeroMQ Context
context = zmq.Context()

#Define the socket using the "Context"
sock = context.socket(zmq.SUB)

#Define subscription and messages with prefix to accept.
sock.setsockopt(zmq.SUBSCRIBE, "1".encode('utf-8')) # sólo aceptas los mensajes con id 1
sock.connect("tcp://localhost:5555")

while True:
	message = sock.recv()
	print(message.decode('utf-8'))