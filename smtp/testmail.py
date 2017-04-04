# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


# Create a text/plain message
msg = MIMEText("Hello World")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Test Message'
msg['From'] = 'jacobj10@localhost'
msg['To'] = 'joshualaurencio@gmail.com'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail('jacobj10@localhost', 'joshualaurencio@gmail.com', msg.as_string())
s.quit()
