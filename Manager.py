from Person import *
class Manager(Person):
    """description of class"""
    def __init__(self,sport='sport', name='name', id='id', password='pass'):
        Person.__init__(self,name,id,password)
        self.sport=sport
        
    def read_from_f(self):
        myf=open('Manager_f.txt','r+')
        tempcont=[]
        temp=[]
        cont=myf.readlines()
        for i in cont:
            temp.append(i.split(','))
        myf.close()
        return temp

    def up_f(self,sport,name,id,password):
        temp=self.read_from_f()
        for i in temp:
            if i[2]==self.ID:
               i[0]=sport
               i[1]=name
               i[2]=id
               i[3]=password
               
               break
        myf=open('Manager_f.txt','w')
        
        for i in temp:
            ret='{},{},{},{}'.format(i[0],i[1],i[2],i[3])
            myf.write(ret)
        myf.write('\n')
        myf.close()
                   


