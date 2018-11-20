# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 23:50:30 2018
@author: Rathin
"""
#This code implements the distortion filter
#It modulates the amplitude and then does the clipping using a given thresold
import pandas as pd
data = pd.read_csv('rathinfinal300500.dat', sep='\s+', header=None, skiprows=2)# read file frmo second line

x=data[0] #read colmn 0
y=data[1] #read coumn 1
xlist=[]  #creating empty list
ylist=[]  #creating empty list
for i in range(0,int(len(x))):
    xlist.append(float(x.iloc[i])) #adding value to xlist 
    ylist.append(float(y.iloc[i])) #adding value to ylist
    
print(len(ylist))                           #printing length of the samples
f= open("rathinoutputfile.dat","w")         #creating a rathinoutputfile.dat and opening in write mode
f.write("; Sample Rate "+ str(44100)+"\n")  #adding header i.e. sample rate
f.write("; Channels 1 "+"\n")               #adding header i.e. channels 
counter=0                                   #counter used to check if any sample are less or missing
for i in range(0, int(len(xlist))):     #for loop for filter and also for writing the data in file
    ylist[i]=ylist[i]*2                 #amplifying the audio
    if ylist[i]>0.316:                  #clipping with thresold value -10db
        ylist[i]=(0.316)                
    elif ylist[i]< (-0.316):            
        ylist[i]= (-0.316)
    
    f.write(str(xlist[i])+"  " + str((ylist[i])) +"\n") #writing the time and amplitude data in the file
    counter=counter+1                                   #checking sample count
print (counter)
f.close()           #closing the file opened for editing
    
