# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:01:26 2022

@author: Philanoe
-- BACK --
Functions for the Multi-context question answering chatbot
"""
from fastapi import FastAPI
import Chatbot

app = FastAPI()
mychat = Chatbot.chatbot()

@app.get("/")
# use async when you do not need to wait for any answer to run the code
async def root():
    return {"message": "Hello World"}

@app.get("/question/")
def EmptyQuestion():
    answer = "Empty Question !"
    return {"question" : "", "answer" : answer}


@app.get("/question/{question_from_frontend}")
def GET_Model_Question_Answering2(question_from_frontend):
    #answer = Chatbot.QuestionAnswering(Model, question)
    answer = "default answer"
    return {"question" : question_from_frontend, "answer" : answer}


@app.get("/classifier/{question_from_frontend}")
def QuestionClassifier(question_from_frontend):
    #label = mychat.Classifier(question)
    label = 0
    return {"question" : question_from_frontend, "label" : label}

@app.get("/Diagnosis/")
def Diagnosis():
    return {f'chatbot message : {str(mychat.Message)}  chatbot error : {str(mychat.Error)}'}