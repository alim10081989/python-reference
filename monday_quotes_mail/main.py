from datetime import datetime as dt
import smtplib
from random import choice

tdate = dt.now()
tday = tdate.weekday()
my_email = "sample@gmail.com"
password = 'dhcbjsvdcjsvdcj'

if tday == 1:
    with open('quotes.txt', encoding='utf8') as file:
        all_quotes = file.readlines()
        quote = choice(all_quotes)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='azim.sheikh3@gmail.com',
                            msg=f'Subject:Monday Motivation\n\n{quote}'.encode('utf8'))
