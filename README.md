## About

This microservice generates and returns health/wellness tips using ZeroMQ.

## Requesting Data

When a user clicks a button on the web interface to receive a health/wellness tip, a ZeroMQ socket is created. 

```
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```

Then, the microservice is sent a health/wellness topic parameter.
`socket.send_string(parameter)`

## Receiving Data

When the microservice receives a request from the client, it generates a health/wellness tip by choosing a random index from a dictionary of health/wellness tip parameters.

`tip = socket.recv_string()`

The tip is then displayed to the user.

## UML Sequence Diagram
