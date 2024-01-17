import schedule, time, os, smtplib # Import the smtp library
import random
from email.mime.multipart import MIMEMultipart # Import the mime library to create multipart messages
from email.mime.text import MIMEText # Import the mime library to create text messages

password = os.environ['mailPassword']
username = os.environ['mailUsername']

def chooseQuote():
  quote = ""
  f = open(".tutorial/quotes.txt", "r")
  quotes = eval(f.read())
  f.close()
  quote = random.choice(quotes)
  return quote

def sendMail():
  email = chooseQuote() # Contents of the message
  server = "smtp.gmail.com" # Address of the mail server, change it to yours if you need to
  port = 587 # Port of the mail server, change it to yours if you need to
  s = smtplib.SMTP(host = server, port = port) # Creates the server connection using the host and port details
  s.starttls() # Sets the encryption mode
  s.login(username, password) # Logs into the email server for us

  msg = MIMEMultipart() # Creates the message
  msg['To'] = "colethompson@comcast.net" # Sets the receiver's email address
  msg['From'] = username # Sets the sender's email address
  msg['Subject'] = "Today's Quote" # Sets the subject of the message
  msg.attach(MIMEText(email, 'html')) # Attaches the email content to the message as html

  s.send_message(msg) # Sends the message
  del msg # Deletes the message from memory

sendMail() # Call the subroutine to test it.

def printMe():
  print("⏰")

schedule.every(1).hours.do(printMe) # Changed the interval to every 1 hour

while True:
  schedule.run_pending()
  time.sleep(1)