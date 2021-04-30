import socket

# Obtenemos el hostname con el método de socket

hostname = socket.gethostname()

print(hostname) # se muestra el hostname o el nombre de la máquina

# Obtenemos la dirección IP

my_ipadd = socket.gethostbyname(hostname)

print((my_ipadd))

