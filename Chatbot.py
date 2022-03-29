# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:01:26 2022

@author: Philanoe
-- BACK --
Functions for the Multi-context question answering chatbot
"""

import os
import pandas as pd
import datasets
from transformers import Trainer, AutoModelForSequenceClassification, AutoTokenizer
from transformers import DataCollatorWithPadding, TrainingArguments, pipeline

class chatbot:
  
    def __init__(self):
        
        self.Error = None
        self.Message = "no message"
        self.label = 43
        
        try:

            os.environ["TOKENIZERS_PARALLELISM"]="true"
            os.environ["WANDB_DISABLED"] = "true"
            
            """ 
            ------------------------------
            Classifier Initialisation
            ------------------------------
            """
            
            ModelPath = "./Data/"
            TokenizerPath = "./Data/"
            
            IntentClassifier = AutoModelForSequenceClassification.from_pretrained(ModelPath,num_labels=4)
            self.IntentTokenizer = AutoTokenizer.from_pretrained(TokenizerPath)
            data_collator = DataCollatorWithPadding(tokenizer=self.IntentTokenizer)
            training_args = TrainingArguments(
                output_dir="./results",
                learning_rate=2e-5,
                per_device_train_batch_size=8,
                per_device_eval_batch_size=8,
                num_train_epochs=7,
                weight_decay=0.01,
                #evaluation_strategy="epoch"
            )
            
            self.trainer = Trainer(
                model=IntentClassifier,
                args=training_args,
                train_dataset=None,
                #eval_dataset=tokenize_test,  Here, we work with the entire dataset as training data
                #compute_metrics=compute_metrics,
                tokenizer=self.IntentTokenizer,
                data_collator=data_collator,
            )
            
            """
            ------------------------------
            Context based Initialization
            ------------------------------
            """
            PipelinePath = './Data/Pipeline'
            self.ContextBasedQuestionAnswerer = pipeline("question-answering", model = PipelinePath, tokenizer = PipelinePath)
            self.Message = "Initialization completed"
            pass
        except Exception:
            self.Error = Exception
            pass
    
            
    def preprocess_function(self, Question):
        return self.IntentTokenizer(Question["sentence"], truncation=True, padding=True)
    
    
    def Classifier(self, Question):
        """ Take a sentence as input, return the corresponding label
    
        use : Tokenizer, Model
        """
        # here, we are keeping the input as a Dataset, which could allow us to reuse the code
        # to answer many questions at once
        QuestionDFData = {'sentence' : [Question]}
        QuestionDataFrame = pd.DataFrame(data = QuestionDFData)
        QuestionDataset = datasets.Dataset.from_pandas(QuestionDataFrame)
        Tokenised_Question = QuestionDataset.map(self.preprocess_function,batched=False)
        
        labelScores =self.trainer.predict(Tokenised_Question)
        Bestlabel = labelScores.predictions.argmax(1)
        
        #IndexTolabel = {0:"Software Recommendation",1:"Make Update",2:"Shutdown Computer",3:"Setup Printer"}
        #OutputlabelName = IndexTolabel[Bestlabel[0]]
        self.label = Bestlabel[0]
        
        return self.label
        
    def UpdateContext(self):
        if(self.label == 0):
            self.Context = "blablabla"
        elif(self.label == 1):
            self.Context == "bliiblibliblisdfsdfx"
        elif(self.label == 2):
            self.Context == "hihihihih"
        elif(self.label == 3):
            self.Context == "hohoho"

    def QuestionAnswerer(self, Question):
    
        answer = self.ContextBasedQuestionAnswerer(Question, self.Context)           
        
        return answer



