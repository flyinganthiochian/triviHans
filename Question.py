from Competitor import *
from Topic import *
from Question import *
from Selection import *
from Game import *
class Question:
    id=0
    def __init__(self,givenTopic,givenText,givenPoint):
        Question.id += 1
        self.id=Question.id
        self.selections=[]
        self.point=givenPoint
        self.text = givenText
        self.topic = givenTopic
        self.correctAnswerLetter=""
        
        givenTopic.questions.append(self)

    def setCorrectAnswer(self):
        for selection in self.selections:
            if selection.isCorrect==True:
                self.correctAnswerLetter=selection.letter
                break

    



    def initalizeScienceQuestions(givenGame):
        #initalize Science Questions
        q1Text="Who is the inventer of the telephone?"
        q1s1= Selection("Marie Curie")
        q1s2= Selection("Rudolph Diesel")
        q1s3= Selection("Alexander Graham Bell")
        q1s4= Selection("Nikola Tesla")

        q1=Question(givenGame.topics[0],q1Text,2)
        Selection.addSelectionToQuestion(q1s1,q1,False)
        Selection.addSelectionToQuestion(q1s2,q1,False)
        Selection.addSelectionToQuestion(q1s3,q1,True)
        
        Selection.addSelectionToQuestion(q1s4,q1,False)
        givenGame.topics[0].unusedQuestions.append(q1)
        
        q2Text="Who is the inventer of the telephone?"
        q2s1= Selection("Marie Curie")
        q2s2= Selection("Rudolph Diesel")
        q2s3= Selection("Alexander Graham Bell")
        q2s4= Selection("Philo Taylor Farnsworth")

        q2=Question(givenGame.topics[0],q2Text,4)
        Selection.addSelectionToQuestion(q2s1,q2,False)
        Selection.addSelectionToQuestion(q2s2,q2,False)
        Selection.addSelectionToQuestion(q2s3,q2,False)
        Selection.addSelectionToQuestion(q2s4,q2,True)
        givenGame.topics[0].unusedQuestions.append(q2)

        #initialize Sports Questions

        q3Text="Which team won in The Final Game of the UEFA Champions League?"
        q3s1= Selection("Barcelona")
        q3s2= Selection("A.C. Milan")
        q3s3= Selection("Real Madrid")
        q3s4= Selection("Bayern München")

        q3=Question(givenGame.topics[1],q3Text,2)
        Selection.addSelectionToQuestion(q3s1,q3,True)
        Selection.addSelectionToQuestion(q3s2,q3,False)
        Selection.addSelectionToQuestion(q3s3,q3,False)
        Selection.addSelectionToQuestion(q3s4,q3,False)
        givenGame.topics[1].unusedQuestions.append(q3)




