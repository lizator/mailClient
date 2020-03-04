import socket
import base64


def sendmsg(msg, response=True):
    clientSocket.send(msg.encode())
    if response:
        recv = clientSocket.recv(1024).decode()
        return recv


subject = "Testing computer networks!"
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
TOMAIL = "smtpcontesting@outlook.com"
FROMMAIL = "testing@dtu.dk"


hostName = "localhost"
mailserver = (hostName, 25)

# Create socket called clientSocket and establish a TCP connection with mailserver

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode()
print("message after connection request: " + recv)

if recv[:3] != '220':
    print('220 reply not received from server.')
    exit(-1)

heloCommand = 'EHLO Alice\r\n' # EHLO for extended SMTP

clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()

print("msg after EHLO: " + recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')


username = "smtpcontesting@outlook.com"
"""
password = "Thunderbird720"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())
"""


# Send MAIL FROM command and print server response.

mailFrom = "MAIL FROM:bhsi@dtu.dk\r\n"
recv2 = "Response after MAIL FROM: " + sendmsg(mailFrom)
print(recv2)

# Send RCPT TO command and print server response.

rcptTo = "RCPT TO: " + username + "\r\n"
recv3 = "Response after RCPT TO: " + sendmsg(rcptTo)
print (recv3)


# Send DATA command and print server response.
data = "DATA\r\n"
sendmsg(data, False)
#recv4 = "Response after 1st DATA: " + sendmsg(data)
#print(recv4)


# Send message data.

sendmsg("Subject:" + subject + "\r\n", False)

msgdata = msg + "\r\n"
sendmsg(msgdata, False)


# Message ends with a single period.

recv4 = "Response after end DATA: " + sendmsg(endmsg)
print(recv4)


# Send QUIT command and get server response.

sendmsg("QUIT", False)


