import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')

# Print list of available methods
print s.system.listMethods()