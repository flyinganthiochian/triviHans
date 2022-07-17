
from Topic import *
class Competitor:
    id=0
    def __init__(self,givenName):
        
        
        Competitor.id +=1
        self.id=Competitor.id
        self.name=givenName
        self.currentScore=0
        self.selectedTopics=[]
        
        
        #print("New Competitor is created with the Name " + self.name + " and the ID= "+ str(self.id))
    def __repr__(self):
        return " ID = "+ str(self.id) + " Name = " + self.name 

    def setCompetitorTopic(givenCompetitor,topic):
        givenCompetitor.selectedTopics.append(topic)

