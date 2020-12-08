#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib, ssl
import os
import subprocess
from datetime import date

today = date.today()

def sendEmail(to, subject, msg):
    try:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        password = "emailtest!123"
        #TIP: for blind input of passowrd use:
        #import getpass
        #password = getpass.getpass()

        # Create a secure SSL context
        context = ssl.create_default_context()

        sender_email = "info.jfragosojanuario@gmail.com"
        receiver_email = to  # Enter receiver address
        deliver_name = "Portolio Monitoring"
        
        message = f'From: {deliver_name}\nTo: {receiver_email}\nSubject: {subject}\n\n{msg}'
        print(message)

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.encode("utf8"))

        print("Email Sent")
    except:
        print("Some Error Occured")

