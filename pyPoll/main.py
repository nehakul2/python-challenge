#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:05:30 2017

@author: nkulkar
"""

import pandas as pd
from pathlib import Path

#ask the user to enter the file he wants to check the results for
input_file = input("Please enter the name of the election input file ? :")
#output_file= input("Please enter the name of the election result output file ?:")
#asigning output filename to create later

output_file = "result_"+input_file

# do a check if the file exists.
file_check =  Path(input_file)
file_exists = file_check.exists()

#execute the process if the file the user mentioned exists.
try:
    file_exists == True
    
    
    #open the file
    myinputfile = input_file
    
    
    
    def result(myfile):
        #open csvfile
        data= pd.read_csv(myfile)
        
        #Lets calculate the total no of votes
        TotalVotes = data['Voter ID'].count()
        print("Total votes in this Elections are :",TotalVotes)
        
        #Lets find the unique candidates
        print(" ")
        print ("Candidates that contested the Ecection are : ", data ['Candidate'].unique())
        print(" ")
        
        #Lets calculate the total votes for each candidate
        list = []
        list= data.groupby('Candidate')['Voter ID'].count()
        
       # Now lets print the list
        ctotal=list.values
        
        # Lets print the total votes per Candidate      
        pertotal=list.values/TotalVotes*100 
      
        #Lets prit the final results
        print(" ")
        print("***--------------------------------***")
        print("Election Results  ")
        print("***--------------------------------***")
        print(" ")
        print("Total Votes:",TotalVotes)
        print("***--------------------------------***")
        print(" ")
        df2 = pd.DataFrame({'Candidate' : list.keys() ,'TotalVotes' :ctotal, 'PercentVote':pertotal})
        print (df2.to_string(index=False))
        i=df2.iloc[df2['TotalVotes'].idxmax()]
        print(" ")
        print("***--------------------------------***")
        print("Winning Candidate is  :",i[0])
        print("***--------------------------------***")
    
        #write to file 
        #new_path = /Users/nkulkar/Desktop/LearnPython/home_work3/result.txt'
        new_path = output_file
        myresult = open(new_path,'w')
        
        myresult.write("Election Results \n***--------------------------------*** \n Total Votes:")
        myresult.write(str(TotalVotes))
        myresult.write("\n ***--------------------------------*** \n ")
        myresult.write( df2.to_string(index=False))
        myresult.write("\n ***--------------------------------***\n Winner :")
        myresult.write(i[0])
        myresult.write("\n ***--------------------------------***")
    
        myresult.close()
       
    result(myinputfile)
 
#inform the user, the filename he entered does not exist.    
except FileNotFoundError:
     print("Whhoops! No such file! Please enter the name of the file you'd like to use.")


