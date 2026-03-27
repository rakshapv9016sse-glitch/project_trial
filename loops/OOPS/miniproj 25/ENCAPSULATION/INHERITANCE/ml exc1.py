class Person:
   def name(self):
      print("name:Raksha")

class Employee(Person):
   def salary(self):
      print("salary:100000")
      
class Manager(Employee):
   def department(self):
      print("department:BME")
a = Manager() 
a.name()
a.salary()
a.department()

        