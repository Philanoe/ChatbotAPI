# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:01:26 2022

@author: Philanoe
-- BACK --
Functions for the Multi-context question answering chatbot
"""

class chatbot:

    def __init__(self):
        try:
            import pickle
            #    FullPath = '/Data/QA.sav'
            #        ContextBasedQuestionAnswerer = pickle.load(open(FullPath,"rb"))
            self.IntentClassifier = None
            self.QuestionAnswerer = None
            self.InitStatus = True
            pass
        except Exception:
            self.InitStatus = False        
            pass
    
    def Classifier(self,Question):
    
        return "Ubuntu"

    def LoadContext(self,Label):
        if(Label == "sldkfjsfd"):
            self.Context = "sdfsdf"
        elif(Label == "sldkfjsfd"):
            self.Context == "sdfsdfx"

    def ContextBasedQuestionAnswering(self, Question):
        Answer = "sdfsdf"
        return Answer

    def QuestionAnswering(self, Question):
    
        Context = "Ubuntu is very good"
        answer = "default answer"
        #answer = ContextBasedQuestionAnswerer.predict(Question,Context)
        answer = f'Your question {Question} was quite interesting, the answer is {answer} !'
    
        return answer



