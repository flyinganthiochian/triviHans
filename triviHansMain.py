#This is the Main module
# |Importing classes|
from Competitor import *
from Game import *
from Topic import *

newGame= Game()

numberOfPlayers=int(input("How Many Players will play? :"))

for player in range(1,numberOfPlayers+1):
    comp = Competitor(input("Player " + str(len(newGame.competitors)+1)+" enter your name: "))
    newGame.addCompetitor(comp)





print("In the first Level you'll be asked ", str(newGame.level1Length)+ " number of Questions")

# This area belongs to tests
print("")
print("***Test are started***")
print("")
# printing Current Topics

#print("Number of players in the game is= "+ str(len(newGame.competitors)))
""" for competitor in newGame.competitors:
    print(competitor) """

print("Number of topics are: " + str(len(newGame.topics)))
print("Number of players are: " + str(len(newGame.competitors)))
#print("Initial topics are: ")

""" for topic in newGame.topics:
    print("Topic ID= " + str(topic.id) + " Title= " + topic.title )
    print("Total Number of Questions in this topics is= " + str(len(topic.unusedQuestions))) 
     for question in topic.questions:
        print ("Question ID= "+ str(question.id) + " Text= " + question.text)
        print("Correct answer is= ", question.correctAnswerLetter)
        print ("Question Point = ", str(question.point)) """

# now printing competitor information,

newGame.playGame()
print("")

print("")
print("***Tests are ended***")
# End of Test codes





