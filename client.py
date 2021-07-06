import socket
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent


chat = []
my_msg = []

with open('config.json') as json_file:
    config = json.load(json_file)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((config['ip'], config['port']))
connection_msg = '\n< ' + config['name'] + ' connected >'
client_socket.sendall(str.encode(connection_msg))
my_msg.append(connection_msg)

with open('template.txt') as file:
    template_reset = file.read()

with open('chat.txt', 'w') as file:
    file.write('<! You logged in as:' + config['name'] + ' !>\n')
    file.write(template_reset)


class ChatHandler(FileSystemEventHandler):
    event = FileModifiedEvent('chat.txt')

    def on_modified(self, event):
        with open('chat.txt') as file:
            lines = file.readlines()
            name_usr = config['name']
            try:
                text_usr = lines[5].strip()
                options = lines[1].strip()
            except IndexError:
                text_usr = ''
                options = ''

            if text_usr != '' and text_usr != my_msg[-1] and name_usr != '':
                client_socket.sendall(str.encode(name_usr + '\t\t > ' + text_usr))


if __name__ == '__main__':
    event_handler = ChatHandler()
    observer = Observer()
    observer.schedule(event_handler, '.', recursive=False)
    observer.start()

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                # break
                raise KeyboardInterrupt
            chat.append(data.decode('utf-8'))
            with open('chat.txt', 'w') as file:
                file.write('<! You logged in as:' + config['name'] + ' !>\n')
                file.write(template_reset)
                for msg in chat:
                    file.write(msg + '\n')

    except KeyboardInterrupt:
        disconnection_msg = '< ' + config['name'] + ' disconnected >'
        client_socket.sendall(str.encode(disconnection_msg))
        my_msg.append(disconnection_msg)
        client_socket.close()
        with open('chat.txt', 'w') as file:
            file.write('')
        observer.stop()
    observer.join()

