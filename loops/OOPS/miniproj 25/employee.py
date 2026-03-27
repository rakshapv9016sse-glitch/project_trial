class employees:
    company="TCS"
    def __init__(self,name,age,department):
        self.name=name
        self.age=age
        self.department=department
a=employees("raksha",20,"BME")
b=employees("conrad",27,"ECE")
print(a.name,a.age,a.department)
print(b.name,b.age,b.department)