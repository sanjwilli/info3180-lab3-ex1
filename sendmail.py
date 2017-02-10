import smtplib

from_addr = ''

to_addr = ''

from_name = ""

to_name = ""

subject = ""

msg = ""

message = """From: {0} <{1}>

To: {2} <{3}>

Subject: {4}

{5}

"""

message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

# Credentails (if needed)

username = ''

password = ''

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com',587)

server.ehlo()

server.starttls()

server.login(username, password)

server.sendmail(from_addr, to_addr, message_to_send)

server.quit()
