from Pregnant_App import ListOfclients
class Add_client:
    def __init__(self, id=1, name="no name", phone_number=123, week_number=1, text="no text", time="no time"):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.week_number = week_number
        self.text = text
        self.start_time = time
        ListOfclients.append(self)


