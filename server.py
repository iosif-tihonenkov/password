import socket
import sqlite3

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2000))

server.listen(4)
print('Сервер запущен')

client_socket, address = server.accept()
#Работаем с БД
conn = sqlite3.connect('logPas.db') #Создаем БД. Если уже есть - подключится
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS logPas(
    servise_name TEXT,
    login TEXT,
    Password TEXT)
""")
conn.commit()
#Получение данных с клиента
data = client_socket.recv(1024).decode('utf-8')
data1 = eval(data)

cur.execute("INSERT INTO logPas VALUES(?,?,?);", data1)
conn.commit()

print('Сервер закончил работу')