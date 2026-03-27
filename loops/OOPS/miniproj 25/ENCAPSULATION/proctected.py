class employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
account=employee("raksha",100000)
print(account._salary)

class manager(employee):
    def show_salary(self):
        print(f"salary:{self._salary}")
    def show_name(self):
        print(f"name:{self._name}")
manage=manager("raksha",100000)
manage.show_salary()
manage.show_name()