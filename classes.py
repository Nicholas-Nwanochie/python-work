# create your own data type
# class = a data type

class Student:
# define what a student is
    def __init__(self, name, major, gpa,is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
# for class object funtion

    def on_honor_roll(self):
      if self.gpa >= 3.5:
         return True
      else:
         return False




