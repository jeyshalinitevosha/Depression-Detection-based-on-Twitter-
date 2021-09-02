# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:36:25 2021

@author: Tevosha Edwards
"""

import kivy
kivy.require("1.10.0") 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.pagelayout import PageLayout
from kivy.base import runTouchApp
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
import nltk
nltk.download('vader_lexicon')
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
import twint 
import nest_asyncio
nest_asyncio.apply()
from kivy.clock import Clock
import pandas as pd
import httplib2
import json
from urllib.request import urlopen
import urllib.request
import numpy as np 
import matplotlib.pyplot as plt 


class ScreenOne(Screen):
    pass
    
    	
class ScreenTwo(Screen):
    pass


class ScreenThree(Screen):
    pass

class ScreenManager(ScreenManager):
    pass



class mainApp(App):
    
    def build(self):
        my_frame = Builder.load_file("main.kv")
        return my_frame
        
    def username(self):
        try:
            username = self.root.get_screen("ScreenTwo").ids.username.text
        
            t = twint.Config()

            t.Search = username
            t.Lang = "en"
            t.Limit = 100
            t.Pandas = True

            twint.run.Search(t)
            ## create the dataframe
            df_user = twint.storage.panda.Tweets_df
        
            sid = SentimentIntensityAnalyzer()
            df_user['scores'] = df_user['tweet'].apply(lambda tweet: sid.polarity_scores(tweet))
        
            df_user['compound'] = df_user['scores'].apply(lambda score_dict: score_dict['compound'])
            df_user['Sentiment']=''
            df_user.loc[df_user.compound>=0,'Sentiment']='Non-Depressive'
            df_user.loc[df_user.compound<0,'Sentiment']='Depressive'
            analysis = ['Non-Depressive', 'Depressive']
        except:
            print ("Error")
            pass
         
                    
        data = df_user.Sentiment.value_counts()        
        #data.plot(kind='pie',title="Tweet Analysis")
        plt.pie(data, labels = analysis, autopct = '%.1f%%')
        plt.savefig('analysis9.png')
        plt.show()
    
    

mainApp().run()