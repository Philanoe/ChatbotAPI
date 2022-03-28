# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:01:26 2022

@author: Philanoe
-- BACK --
Functions for the Multi-context question answering chatbot
"""

# prepare a global variable for the model
ContextBasedQuestionAnswerer = None
#InitStatus = False

def Init():
    global ContextBasedQuestionAnswerer
#    FullPath = '/Data/QA.sav'
#    import pickle
#    try:
#        ContextBasedQuestionAnswerer = pickle.load(open(FullPath,"rb"))
#        InitStatus = True
#         pass
#    except Exception:
#        InitStatus = False
#        pass        
#       
#    return InitStatus

def Classifier(Question):
    
    return "Ubuntu"

def LoadContext(Label):
    if(Label == "sldkfjsfd"):
        Context = "sdfsdf"
    elif(Label == "sldkfjsfd"):
        Context == "sdfsdfx"
    return Context

def ContextBasedQuestionAnswering(Question, Context):
    Answer = "sdfsdf"
    return Answer

def QuestionAnswering(Question):
    
    Context = "Ubuntu is very good"
    global ContextBasedQuestionAnswerer
    answer = "default answer"
    #answer = ContextBasedQuestionAnswerer.predict(Question,Context)
    answer = f'Your question {Question} was quite interesting, the answer is {answer} !'
    
    return answer



