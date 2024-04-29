import re
import sys
import os
import numpy
import pandas as pd
import json
from API.connectDB import *


def get_gui_data(message, keywords):
    dictData = {
        "user_id": 1,
        "msg": "Filler",
        "keywords": "",
        "delay": 1
        }
    keyword_list = []
    cleaned_message = ""

    
    split_keywords = keywords.splitlines()
        
    for line in split_keywords:
        number, keyword = line.split(": ")
        keyword_list.append(keyword)
    
    message_split = message.splitlines()
    cleaned_message = '\n'.join([line.split(': ')[1] for line in message_split])
    
    keyword_string = ', '.join(keyword_list)
    
    # Adding to the dictionary
    dictData["msg"] = cleaned_message
    dictData["keywords"] = keyword_string
    
    addingInfoDB(dictData)
    #print("This is the information {0}, {1}".format(cleaned_message, listKeyW))
    
def addingInfoDB(dictData):
    cnx = connect_db()
    
    if cnx:  
        add_basic_message(cnx, dictData)
    else:
        print("Error connecting")
            