from . import protocols

def process(user: protocols.User):
    for connection in user.connections:
        print(connection.service)
