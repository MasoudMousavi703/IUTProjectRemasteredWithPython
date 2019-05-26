from Athlete import *
class FootballPlayer(Athlete):
    """creates a football player as an athlete with additotional attributes"""
    def __init__(self,university='iut',name='name',id='id',password='pass'):
        pass
        Athlete.__init__(self,university,name,id,password)

    def add_to_f(self):
        myf=open('Fplayers_f.txt','r+')
        tempcont=[]
        temp=[]
        cont=myf.readlines()
        for i in cont:
            temp.append(i.split(','))
        tempcont=[i[2] for i in temp]
        if not self.ID in tempcont:
           myf.close()
           myf=open('Fplayers_f.txt','a')
           ret='\n{},{},{},{}'.format(self.university,self.name,self.ID,self.password)
           myf.write(ret)
           return True
        else:
            return False

    def read_from_f(self):
        myf=open('Fplayers_f.txt','r+')
        tempcont=[]
        temp=[]
        cont=myf.readlines()
        for i in cont:
            temp.append(i.split(','))

        return temp

    

