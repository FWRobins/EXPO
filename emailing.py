import pyautogui
import os
import time
import keyboard
import datetime
from datetime import date, timedelta
from easygui import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mimetypes
import email.mime.application
import smtplib


def send_email(address, attach):
    from_email= #removed for security purposes
    from_password= #removed for security purposes
    to_email=address
    subject='PNA 2020 EXPO REGISTRATION'

    message="""\
    <html>
        <head></head>
        <body>
            <p>Good Day</p>
            <p>Thank you for registering for the 2020 PNA Expo.</p>
            <p>Please find attachech the documents you need to print out and bring on the day of the Expo.<p>
            <p>This document entitles you to enry to the Expo and a goodie bag.<p>
            <p>Greetings</p>
            <image src='https://i.imgur.com/iRJ0Pe8.png'></image>
            </body>
    </html>
    """

    msg = MIMEMultipart()
    txt=MIMEText(message, 'html')
    msg["Subject"]=subject
    msg["To"]=to_email
    msg["From"]=from_email
    msg["Cc"]=from_email
    msg.attach(txt)

    filename = str(attach)+".docx"
    fo = open('./docs/'+str(attach)+".docx", 'rb')
    file = email.mime.application.MIMEApplication(fo.read(),_subtype="docx")
    fo.close()
    file.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(file)

    emacc=smtplib.SMTP('smtp-mail.outlook.com', 587)
    emacc.ehlo()
    emacc.starttls()
    emacc.login(from_email, from_password)
    emacc.send_message(msg)


# send_email(BranchList[Branch][1])
