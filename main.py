import datetime as dt
import pandas as pd
import random
import smtplib


MY_EMAIL = ""
MY_PASSWORD = ""
letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
today = (dt.datetime.now().month, dt.datetime.now().day)

df = pd.read_csv("birthdays.csv")

birthday_dict = {(row["month"], row["day"]): row for (index, row) in df.iterrows()}
print(birthday_dict)

if today in birthday_dict:
    rand_letter = random.choice(letters_list)
    birthday_person = birthday_dict[today]
    with open(f"letter_templates/{rand_letter}") as le:
        text = le.read()
        letter = text.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{letter}")




