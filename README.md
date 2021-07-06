Learning English with flashcards.

The project used:
* The [socket package](https://docs.python.org/3/library/socket.html) was used send msg and 
as an engine.
* The [watchdog package](https://pypi.org/project/watchdog/) was used for display and visualization.

To start, you need to register the SP address and port of the server in the server.py file. Then run this file.
Next, you need to have 4 files on the client side: chat.txt, template.txt, config.json, client.py. In the config.json file in the dictionary, you must specify the server type and port.
To start the chat, you need to run the file on the server (server.py). Next, run the client.py file on the client side. Then the template appears in the chat.txt file. In the line after input, enter the text of the message. When saved, the message is sent to all recipients.