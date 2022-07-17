class Selection:
    
    def __init__(self,givenText):
        self.text=givenText
        
        
        
    def addSelectionToQuestion(givenSelection, givenQuestion, isCorrect):
        
        #print("question ID= " + str(givenQuestion.id))
        #print("Number of selections in this Question is= " + str(len(givenQuestion.selections)))
        
        letter="A"
        #print("current letter[0]= " + letter[0])
        
        if len(givenQuestion.selections)>0:
            numberOfSelections = len(givenQuestion.selections)
            lastSelectionLetter= givenQuestion.selections[numberOfSelections-1].letter
            #print("lest Selection Letter is= " + lastSelectionLetter)
            letter = chr(ord(lastSelectionLetter[0]) + 1)
        #print("Letter is = " + letter)
        givenSelection.letter=letter
        givenSelection.question=givenQuestion
        givenSelection.isCorrect=isCorrect
        givenQuestion.selections.append(givenSelection)
        givenQuestion.setCorrectAnswer()
        


            