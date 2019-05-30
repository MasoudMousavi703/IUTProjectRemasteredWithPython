from Athlete import *
class PingPongPlayer(object):
    """creates a ping pong player as an athlete with wins and losses"""
    def __init__(self,wins=0,losses=0,university='iut',name='name',id='id',password='pass'):
        Athlete.__init__(self,university,name,id,password)
        self.wins=wins
        self.losses=losses
        self.points=self.wins*3-self.losses

    def add_to_f(self):
        myf=open('Pplayers_f.txt','r+')
        tempcont=[]
        temp=[]
        cont=myf.readlines()
        for i in cont:
            temp.append(i.split(','))
        tempcont=[i[2] for i in temp]
        if not self.ID in tempcont:
           myf.close()
           myf=open('Pplayers_f.txt','a')
           ret='{},{},{},{},{},{},{}'.format(self.university,self.name,self.ID,self.password,self.wins,self.losses,self.points)
           myf.write(ret)
           myf.write('\n')
           myf.close()
           return True
        else:
            myf.close()
            return False

    def read_from_f(self):
        myf=open('Pplayers_f.txt','r+')
        tempcont=[]
        temp=[]
        cont=myf.readlines()
        for i in cont:
            temp.append(i.split(','))
        myf.close()
        return temp

    def up_f(self,bal):
        if bal==1:
            self.wins+=1
            print(self.wins)
        elif bal==-1:
            self.losses-=1
            
        self.points=self.wins*3-self.losses
        temp=self.read_from_f()
        for i in temp:
            count=0
            if i[2]==self.ID:
               i[4]=str(self.wins)
               i[5]=str(self.losses)
               i[6]=str(self.points)
               count=1
               break
         
        if count==0:
            return False

        myf=open('Pplayers_f.txt','w')
        for i in temp:
            ret='{},{},{},{},{},{},{}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            myf.write(ret)
            myf.write('\n')
        myf.close()
        return True