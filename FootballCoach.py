from Person import *
class FootballCoatch(Person):
    """description of class"""
    def __init__(self,name,id,password,team_id='95',footballList=None):
        self.team_id=team_id
        self.footballList=footballList
        Person.__init__(name,id,password)

    def add_to_f(self):
        myf=open('FootballTeams_f.txt','r+')
        tempcont=[]
        temp=[]
        cont=myf.readlines()
        for i in cont:
            temp.append(i.split(','))
        tempcont=[i[2] for i in temp]
        if not self.team_id in tempcont:
           myf.close()
           myf=open('FootballTeams_f.txt','a')
           ret='{},{},{},{}'.format(self.ID,self.university,self.team_id)
           
           for i in self.footballList:
               ret+=',{}'.format(i)
           myf.write(ret)
           myf.write('\n')
           myf.close()
           return True
        else:
            myf.close()
            return False

    def set_footballList(self):
        tempfootballList=[]
        while True:
            tempfootballList.append(input('Enter ID for players: '))
            control=input('Continue? Y or N: ')
            if control=='N':
                break

        self.footballList=tempfootballList
