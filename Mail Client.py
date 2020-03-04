import socket
import base64


def sendmsg(msg):
    clientSocket.send(msg.encode())
    recv = clientSocket.recv(1024).decode()
    return recv


msg = "\r\n I love computer networks!"

endmsg = "\r\n.\r\n"

hostName = "smtp-mail.outlook.com"
mailserver = (hostName, 587)


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
password = "Thunderbird720"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())



# Send MAIL FROM command and print server response.

mailFrom = "MAIL FROM:bhsi@dtu.dk\r\n"
recv2 = "Response after MAIL FROM: " + sendmsg(mailFrom)
print(recv2)

# Send RCPT TO command and print server response.

rcptTo = "RCPT TO: " + username + "\r\n"
recv3 = "Response after RCPT TO: " + sendmsg(rcptTo)
print (recv3)


# Send DATA command and print server response.
data = "DATA"
recv4 = "Response after 1st DATA: " + sendmsg(data)
print(recv4)


# Send message data.

msgdata = msg + "\r\n"
recv5 = "Response after msg DATA: " + sendmsg(msgdata)
print(recv5)


# Message ends with a single period.

recv6 = "Response after end DATA: " + sendmsg(endmsg)
print(recv6)


# Send QUIT command and get server response.

quitmsg = "QUIT"
recv7 = "Response after 3rd DATA: " + sendmsg(quitmsg)
print(recv6)


