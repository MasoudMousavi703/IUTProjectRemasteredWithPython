from Person import *
class Athlete(Person):
    """creates an athlete as a child for person with additional university data"""

    def __init__(self,university='iut',name='name',id='id',password='pass'):
        self.university=university
        Person.__init__(self,name,id,password)
    def get_university(self):
        return self.university
