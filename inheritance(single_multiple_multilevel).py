#Single Inheritance

class father():
    def person(self):
        print("I am ram's Father")


class son(father):#son name ram
    def person1(self):
        print("I am Ram")

obj=son()
obj.person()
obj.person1()

#Multiple Inheritance

class father():
    def person(self):
        print("I am ram's Father")

class mother():
    def person1(self):
        print("I am ram's Mother")

class son(father,mother):#son name ram
    def person2(self):
        print("I am Ram")

obj=son()
obj.person()
obj.person1()
obj.person2()

#Multilevel-Inheritance

class grandfather():
    def oldperson(family):
        print("I am Rahul's Father")

class father(grandfather):#father name is rahul
    def person(family):
        print("I am Rahul and Ram's Father")


class son(father):#son name ram
    def person1(family):
        print("I am Ram")
        
obj=son()
obj.person1()
obj.person()
obj.oldperson()

obj=father()
obj.person()
obj.oldperson()


        
        






        



