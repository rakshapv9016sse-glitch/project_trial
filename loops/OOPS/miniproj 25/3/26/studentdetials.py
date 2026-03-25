class student:
    def __init__(self,name,mark,department,course,register_number,city,phone_number):
        self.name=name
        self.mark=mark
        self.department=department
        self.course=course
        self.register_number=register_number
        self.city=city
        self.phone_number=phone_number
    def display(self):
        print("student:","details")
        print("name:",self.name)
        print("mark:",self.mark)
        print("department:",self.department)
        print("course:",self.course)
        print("register_number:",self.register_number)
        print("city:",self.city)
        print("phone_number",self.phone_number)
r=student("raksha",90,"BME","python",192319016,"chennai",7806957556)
h=student("harini",95,"BME","python",192319022,"theni",6380534848)
r.display()
h.display()