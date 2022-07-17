class Topic:
    id=0
    def __init__(self, givenTitle):
        Topic.id +=1
        self.id =Topic.id
        self.questions=[]
        self.title = givenTitle
        self.unusedQuestions=[]
        self.usedQuestions=[]
        
    def addTopicToGame(self, givenGame):
        givenGame.topic.append(self)
    def initializeGameTopics(givenGame):
        topicScience= Topic("Science and Technology")
        givenGame.topics.append(topicScience)
        
        topicSports= Topic("Sports")
        givenGame.topics.append(topicSports)

        topicSports= Topic("Literature")
        givenGame.topics.append(topicSports)

        topicSports= Topic("Movies and T.V.")
        givenGame.topics.append(topicSports)
    

