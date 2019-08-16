from Functions import *
import datetime
Dt = datetime.date.today()
ListOfclients = []

if __name__ == "__main__":
    try:
        option = "a"
        id = 1
        while str.lower(option) != "exit":
             print("select option")
             print("1: Add client")
             print("2: save data")
             print("3: check week")
             print("4: Send Sms")
             option = input('enter selection : ')
             if str(option) == "1":
                Add_client(id, Dt)
                id += 1
                print("thank you client have been added")
             elif str(option) == "2":
                save_data()
             elif str(option) == "3":
                check_week(Dt)
             elif str(option) == "4":
                 Sendsms("972528021250", "תרים לנגיחה")
             elif str(option) == "5":
                 add_text(2)

        print("thank you good bye")
    except Exception as e:
        print("error in main", e)