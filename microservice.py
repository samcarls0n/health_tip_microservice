import zmq
import random
from tips import tips


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Server started...")

while True:
    # Await request from client
    parameter = socket.recv().decode()

    # Generate tip based on parameter received
    if parameter in tips:
        tip = random.choice(tips[parameter])
    else:
        tip = "Sorry, no tip available for this parameter."

    # Send tip back to the client
    socket.send_string(tip)
