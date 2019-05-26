class Person(object):
    """creates a person with name, ID and password"""
    def __init__(self,name='name',id='id',password='pass'):
        self.name=name
        self.ID=id
        self.password=password

    def set_name(self,name):
        self.name=name

    def set_ID(self,id):
        self.ID=id

    def set_password(self,password):
        self.password=password

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_ID(self):
        return self.ID

