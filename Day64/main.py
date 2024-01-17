class job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

class doctor(job):
  def __init__(self,experience,specialty):
    self.name = "Doctor"
    self.salary = 150000
    self.hoursWorked = 50
    self.experience = experience
    self.specialty = specialty

class teacher(job):
  def __init__(self,subject,position):
    self.name = "Doctor"
    self.salary = 150000
    self.hoursWorked = 50
    self.subject = subject
    self.position = position

jim = doctor("7", "Paediatric Consultant")
print(jim.experience,jim.specialty)

leane = teacher("Computer Science", "Teacher")
print(leane.subject, leane.position)
