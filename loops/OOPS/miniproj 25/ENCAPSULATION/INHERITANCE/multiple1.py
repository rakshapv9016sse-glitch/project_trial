class father:
    def skills_father(self):
        print("father's skills:working")
class mother:
    def skills_mother(self):
        print("mother's skills:driving")
class child(father,mother):
    def skills_child(self):
        print("child's skills:baking")
a=child()
a.skills_father()
a.skills_mother()
a.skills_child()