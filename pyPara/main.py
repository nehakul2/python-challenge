#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 21:24:52 2017

@author: nkulkar
"""
import re
from pathlib import Path

#path of the file is : /Users/nkulkar/Desktop/LearnPython/home_work3
input_file = input("Please enter the path and name of the Election  file to be analyzed ? :")

file_check =  Path(input_file)
file_exists = file_check.exists()
#print (file_exists)

try:
    file_exists == True
    #if file_exists is True:
    #open the file
    myinputfile = input_file
    file=open(myinputfile,"r+")
    
    #inialize variables 
    wordcount={}
    g_wordcount = 0
    char_count = 0
    
    #Start the loop to get the counts
    for word in file.read().split():       
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
               
    for k,v in wordcount.items():
        lineCount = len(re.split(".",myinputfile))
        g_wordcount = g_wordcount + v
        char_count = char_count + len(k)
       
    # lets print the summary counts
    print("Lets print the results :")
    print ("  ")
    print ("Total word count is  :" + str(g_wordcount))
    print ("  ")
    print ("Total charaxcters are :" + str(char_count))
    print ("  ")
    print ("Total lines are  : " + str(lineCount))
    print ("  ")
    print ("Average sentence length is :" , (char_count/lineCount))
    print ("  ")
    print ("Average word lenth  is : " , (char_count /g_wordcount))
    print ("  ")

except FileNotFoundError:
     print("Whhoops! No such file! Please enter the name of the file you'd like to use.")

