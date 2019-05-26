from Person import *
class Athlete(Person):
    """description of class"""

    def __init__(self,university='iut',name='name',id='id',password='pass'):
        self.university=university
        Person.__init__(self,name,id,password)
    def get_university(self):
        return self.university