from xmlrpc.server import SimpleXMLRPCServer
from board import Board


# Restrict to a particular path.
server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)


# Create server
server.register_introspection_functions()
server.register_instance(Board())
print("serving...")
# Run the server's main loop
server.serve_forever()
