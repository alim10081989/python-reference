from random import randint
from datetime import datetime as dt
import pandas
import smtplib

my_email = "sample@gmail.com"
password = 'jdhbcjsdbcjs'

tdate = dt.now()
today = (tdate.month, tdate.day)

data = pandas.read_csv('birthdays.csv')
birthday_dict = {(row['month'], row['day']): row for (index, row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    print(birthday_person)
    file_path = f'letter_templates/letter_{randint(1,3)}.txt'

    with open(file_path) as letter_file:
        contents = letter_file.read()
        final_letter = contents.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person['email'],
                            msg=f'Subject:Happy Birthday\n\n{final_letter}')
