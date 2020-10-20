#alejandro ortega
import datetime, time

class Age:

  myDay   = 0
  myMonth = 0
  myYear  = 0
  currentDay   = 0
  currentMonth = 0
  currentYear  = 0

  def __init__(self, name):
    self.name = name
    self.splitBday()
    self.setDay()
    self.setMonth()
    self.setYear()

  def splitBday(self):
    flag = True
    while(flag):
      dob = input("What is your date of birth?\nUse MM/DD/YYYY format.\n$ ")
      splitter = dob.split("/")
      if(len(dob) == 10):
        if(dob[2] == "/" and dob[5] == "/"):
          self.myMonth = splitter[0]
          self.myDay   = splitter[1]
          self.myYear  = splitter[2]  
          flag = False
      else:
        print("* * * Use correct format * * *")
        flag = True

  def todaysDate(self):
    return datetime.date.strftime(datetime.date.today(), "%m/%d/%Y")

  def setDay(self):
    self.currentDay = datetime.date.today().day
  
  def setMonth(self):
    self.currentMonth = datetime.date.today().month

  def setYear(self):
    self.currentYear = datetime.date.today().year

  def getAge(self):
    age = 999
    if(int(self.myMonth) > self.currentMonth):
      age = (self.currentYear - int(self.myYear)) - 1
    elif(int(self.myMonth) <= self.currentMonth):
      if(int(self.myDay) > self.currentDay):
        age = (self.currentYear - int(self.myYear)) - 1
      else:
        age = self.currentYear - int(self.myYear)

    print(self.name ,", you are ", age ," years old.")

try:
  name = input("What is your name?\n$ ")
  a1 = Age(name)
  print("Today's a beautiful day!\nToday's date: ", end = "")
  print(a1.todaysDate())
  print("One second...")
  time.sleep(3)
  a1.getAge()
except:
  print("Issue will get fixed.")