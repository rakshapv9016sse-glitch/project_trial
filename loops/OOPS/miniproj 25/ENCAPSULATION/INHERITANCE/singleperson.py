class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_info(self):
        print(f"name:{self.name},age:{self.age}")
class Employee(person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def show_employee_info(self):
        print(f"name:{self.name},age:{self.age},salary:{self.salary}")
emp=Employee("raksha",20,100000)
emp.show_info()
emp.show_employee_info()
