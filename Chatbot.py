# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:01:26 2022

@author: Philanoe
-- BACK --
Functions for the Multi-context question answering chatbot
"""

# prepare a global variable for the model
ContextBasedQuestionAnsweringModel = None

def Init():
    import pickle
    global ContextBasedQuestionAnsweringModel
    FullPath = '/Data/QA.sav'
    ContextBasedQuestionAnsweringModel = pickle.load(open(FullPath,"rb"))

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
    global ContextBasedQuestionAnsweringModel
    answer = ContextBasedQuestionAnsweringModel.predict(Question,Context)
    answer = f'Your question {Question} was quite interesting, the answer is {answer} !'
    
    return answer



