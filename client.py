import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    # Prompt the user to enter a wellness topic
    parameter = input("Enter a parameter (e.g., age, nutrition), or type 'quit' to quit: ")

    if parameter.lower() == "quit":
        break

    # Send the parameter to the server
    socket.send_string(parameter)

    # Receive and print the wellness tip from the server
    tip = socket.recv_string()
    print("Tip:", tip)

print("Exiting...")
