import smtplib

from_addr = 'williamsanjay123@gmail.com'

to_addr = 'williamsanjay12@gmail.com'

from_name = "Sanjay"

to_name = "Sanjay"

subject = "Testing"

msg = "Testing this thing again"

message = """From: {0} <{1}>

To: {2} <{3}>

Subject: {4}

{5}

"""

message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

# Credentails (if needed)

username = 'williamsanjay123@gmail.com'

password = 'dljlcgflwzsrofzd'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com',587)

server.ehlo()

server.starttls()

server.login(username, password)

server.sendmail(from_addr, to_addr, message_to_send)

server.quit()

# dljlcgflwzsrofzd 