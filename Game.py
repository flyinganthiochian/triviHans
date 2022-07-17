
import random
from Competitor import *
from Topic import *
from Question import *
from Selection import *
class Game:
    print("Welcome to TriviHans Game")
    currentCompetitor=0
    def __init__(self):
        self.competitors=[]
        self.topics=[]
        self.totalNumberOfLevels=3
        
        self.level1Length=10
        self.playingOrder=[]
        Game.initializeGameTopics(self)
        Game.initalizeGameQuestions(self)
        
    def addCompetitor(self, givenCompetitor):
        self.competitors.append(givenCompetitor)
        #print(givenCompetitor.name + " has Joined the game")
        Game.currentCompetitor +=1

    #game initialization codes Starts Here
    def initializeGameTopics(self):
        Topic.initializeGameTopics(self)
        
    def initalizeGameQuestions(self):
        Question.initalizeScienceQuestions(self)

    def playGame(self):
        self.setPlayerOrder()
        self.setAllCompetitorTopics()


        

         
    
    def setPlayerOrder(self):
        playerPool=self.competitors
        while len(playerPool)>0:
            #print("number of players in the player pool is= "+str(len(playerPool)) )

            choosenPlayer=random.randint(0,len(playerPool)-1)
            self.playingOrder.append(playerPool[choosenPlayer])
            playerPool.remove(playerPool[choosenPlayer])
        self.currentCompetitor=self.playingOrder[0]
        print(" Playing Order: ")
        for player in self.playingOrder:
            print(player.name)
    def setCurrentCompetitorToNext(self):
        print("current competitor was: "+ self.currentCompetitor.name)
        print("")
        if self.currentCompetitor == self.playingOrder[len(self.playingOrder)-1]:
            self.currentCompetitor = self.playingOrder[0]
        else:

            self.currentCompetitor = self.playingOrder[self.playingOrder.index(self.currentCompetitor)+1]
        print("But now the current Competitior is: "+ self.currentCompetitor.name)
    
    def setAllCompetitorTopics(self):

        for player in self.playingOrder:
            print("Hello "+ player.name + " here are your topics")
            for topic in self.topics:
                print("ID= "+ str(topic.id) + " | Title= "+topic.title)
            selectedTopicID= input("Please Enter the ID of your Topic Selection: ")
            player.setCompetitorTopic(self.topics[int(selectedTopicID)-1])
            print("")
            print("You have Selected ID= "+str(selectedTopicID)+" Title is= "+ player.selectedTopics[0].title)




        



        
        
        


        


    


