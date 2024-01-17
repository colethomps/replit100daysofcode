import requests
from bs4 import BeautifulSoup
import schedule
import time
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from replit import db  # Import the database

# Function to send an email
def send_email(product_url, desired_price, current_price):
    email_content = f"The price for the product ({product_url}) has dropped to ${current_price}. You desired to buy it for ${desired_price}."

    server = "smtp.gmail.com"  # Address of the mail server, change it to yours if you need to
    port = 587  # Port of the mail server, change it to yours if you need to

    s = smtplib.SMTP(host=server, port=port)  # Creates the server connection using the host and port details
    s.starttls()  # Sets the encryption mode
    s.login(username, password)  # Logs into the email server

    msg = MIMEMultipart()  # Creates the message
    msg['To'] = "your_email@example.com"  # Sets the receiver's email address
    msg['From'] = username  # Sets the sender's email address
    msg['Subject'] = "Product Price Alert"  # Sets the subject of the message

    # Attaches the email content to the message as html
    msg.attach(MIMEText(email_content, 'html'))

    s.send_message(msg)  # Sends the message
    del msg  # Deletes the message from memory
    s.quit()  # Quits the email server

# Function to scrape the product price and check for changes
def check_item():
    url = "https://www.example.com/product-page"  # Replace with the URL of the product you want to track
    desired_price = 50.0  # Set your desired price here

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # Find the current price on the page (you may need to inspect the page source to get the correct element)
    current_price_element = soup.find("span", {"class": "current-price"})
    if current_price_element:
        current_price = float(current_price_element.text.strip().replace("$", ""))
    else:
        current_price = 0.0

    # Load the previous price from the database
    previous_price = db.get("previous_price", None)

    # Check if the price has changed and is below the desired price
    if current_price != previous_price and current_price < desired_price:
        send_email(url, desired_price, current_price)

    # Update the previous price in the database
    db["previous_price"] = current_price

# Your Gmail credentials
username = "your_email@gmail.com"  # Your Gmail email address
password = "your_password"  # Your Gmail password

# Schedule the price check to run every day at a specific time (e.g., 8:52 AM)
schedule.every().day.at("08:52").do(check_item)

while True:
    schedule.run_pending()
    time.sleep(1)
