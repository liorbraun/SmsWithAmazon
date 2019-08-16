from Add_client_class import Add_client
from Amazon_Connection import AmazonSendSms
from Pregnant_App import ListOfclients
import pandas as pd
import csv
import datetime
errorTime = datetime.date.today()

def add_client(id ,time):
  try:
    name = input('Enter Name:')
    phone_number = int(input('Enter phone number:'))
    week_number = int(input('whats your week? : '))
    date = time
    text = add_text(week_number)
    Add_client(id, name, phone_number, week_number, text, date)
  except:
    print("error in add client")

def save_data():
  try:
    with open("data.csv", 'w', newline='',encoding="utf-8") as csf:
     writer = csv.writer(csf)
     writer.writerow(['id', 'name', 'phone_number', 'week_number', 'text', 'start_time'])
     for savedata in ListOfclients:
       writer.writerow([savedata.id, savedata.name, savedata.phone_number, savedata.week_number, savedata.text, savedata.start_time])
     csf.close()
  except:
    print("error in save_data")

def check_week(Dt):
  try:
    for check_client_time in ListOfclients:
      if Dt - check_client_time.start_time == 7:
         check_client_time.start_time = Dt
         check_client_time.week_number += 1
         check_client_time.text = str(add_text(check_client_time.week_number))
         sendsms(check_client_time.phone_number, check_client_time.text)
  except:
   print("error in check week")

def add_text(week_number):
 try:
   cs = pd.read_csv("test1.csv")
   textforweek = cs["Week"][week_number-1]
   return textforweek
 except:
        print("error in add text")

def sendsms(phoneNumber,message):
    AmazonSendSms(phoneNumber, message)







