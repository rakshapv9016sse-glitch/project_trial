class car:
    def __init__(self,brand,colour,number,model):
        self.brand=brand
        self.colour=colour
        self.number=number
        self.model=model

r=car("MG","maroon",2612,2025)
d=car("BMW","black",2607,2026)

print(r.brand,":",r.colour,":",r.number,":",r.model)
print(d.brand,":",d.colour,":",d.number,":",d.model)
