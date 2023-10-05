import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 2000))


service_name = input('Введите название сервиса: ')
service_login = input('Введите логин: ')
service_password = input('Введите пароль: ')

result = (service_name, service_login, service_password)

for res in result:
    res = str(res)
    client.sendall(bytes(res, 'utf-8'))    
    
data = client.recv(1024).decode('utf-8')



client.close()