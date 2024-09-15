##################### Extra Hard Starting Project ######################


# 2. Check if today matches a birthday in the birthdays.csv

import datetime  as dt
import pandas as pd
import random
import smtplib

my_mail = "samarpittrivediofficial@gmail.com"
password = "blwf vcps hshd huwk"


today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv('birthdays.csv')
birthday_dict = {
    (data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()
}


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

file_path =  f"letter_templates/letter_{random.randint(1,3)}.txt"
if  today  in birthday_dict:
    birthday_person = birthday_dict[today]
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents =  contents.replace("[NAME]", birthday_person["name"])
        print(contents)


# 4. Send the letter generated in step 3 to that person's email address.

    with  smtplib.SMTP('smtp.gmail.com') as smtp:
        smtp.starttls()
        smtp.login(my_mail, password)
        smtp.sendmail(from_addr=my_mail,
                      to_addrs=birthday_person["email"],
                      msg=f"Subject:HAPPY BIRTHDAY \n\n {contents}"
                          )
        smtp.close()


