import zmq
import time
import random

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555") # comunicación a través del puerto lógico 5555

id = 0

while True:
	time.sleep(1)
	id, now = id+1, time.strftime('%H:%M:'+str(random.randint(1,60))) # varían los segundos unicamente

	# Message [prefix][message]
	message = "1-Update! >> {id} >> {time}".format(id=id, time=now) # envías un mensaje con id 1
	socket.send(message.encode('utf-8'))

	# Message [prefix][message]
	message = "2-Update! >> {id} >> {time}".format(id=id, time=now) # envías un mensaje con id 2
	socket.send(message.encode('utf-8'))

	id += 1 # aunmentas el id para el siguiente mensaje, va por numeros impares