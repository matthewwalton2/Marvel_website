#!/usr/bin/env python
# coding: utf-8

# In[71]:

#a program to take the output files from DataScraping.py, in a subfolder "Scraped" and make an output file


import sys
import csv
import os


# In[72]:


fileName = "Wade_Wilson_(Earth-616)_output.txt"


# In[75]:


def singleFileRead(fileName, name, id):
    
    #The columns we are looking to pull out of the scraped data
    Name = ''
    Affiliation = ''
    Marital_Status = ''
    Gender = ''
    Height = ''
    Weight = ''
    Eyes = ''
    Hair = ''
    Unusual_Features = ''
    Origin = ''
    Living_Status = ''
    Reality = ''
    Place_of_Birth = ''
    Identity = ''
    Citizenship = ''
    Occupation = ''
    Creator1 = ''
    Creator2 = ''
    First = ''
    
    #blob is a big mess of tags that are haphazardly added to each page on the marvel wiki, anything from duplicates of the above to their powers to any of the creators or their favorite food
    Blob = ''
    
    Name = name.split("_output.txt")[0]
    #get character name from the input file
    
     #open the input file and break up by tabs then commas, as done by the 
    with open(fileName,'r') as tsvin:
        for line in csv.reader(tsvin, delimiter='\t'):
            for categories in csv.reader(line, delimiter = ','):
                if(not categories):
                    continue
                #if we see the telltale sign of a blob, start adding to it
                elif(categories[0] == "Characters"):
                    for item in categories:
                        Blob += item
                        Blob += '|'
                    break
                #otherwise keep an eye out for the flags of the data we know
                else:
                    for num, item in enumerate(categories, start=0):
                        try:
                            if(item == 'Affiliation'):
                                Affiliation = categories[num + 1]
                            if(item == 'Marital Status'):
                                Marital_Status = categories[num + 1]
                            if(item == 'Gender'):
                                Gender = categories[num + 1]
                            if(item == 'Height'):
                                Height = categories[num + 1]
                            if(item == 'Weight'):
                                Weight = categories[num + 1]
                            if(item == 'Eyes'):
                                Eyes = categories[num + 1]
                            if(item == 'Hair'):
                                Hair = categories[num + 1]
                            if(item == 'Unusual Features'):
                                Unusual_Features = categories[num + 1]
                            if(item == 'Origin'):
                                Origin = categories[num + 1]
                            if(item == 'Living Status'):
                                Living_Status = categories[num + 1]
                            if(item == 'Reality'):
                                Reality = categories[num + 1]
                            if(item == 'Place of Birth'):
                                Place_of_Birth = categories[num + 1]
                            if(item == 'Identity'):
                                Identity = categories[num + 1]
                            if(item == 'Occupation'):
                                Occupation = categories[num + 1]
                            if(item == 'First'):
                                First = categories[num + 1].split('(')[0]
                            if(item == 'Creators'):
                                Creator1 = categories[num + 1]
                                if(categories[num + 2] != 'First'): Creator2 = categories[num + 2]
                        except IndexError:
                            continue
    #print the csv tables into the file
    print(str(id) + ',' + str(Name) + ',' + str(Affiliation) + ',' + str(Marital_Status) + ',' + str(Gender) + ',' + str(Height) + ',' + str(Weight) + ',' + str(Eyes) + ',' + str(Hair) + ',' + str(Unusual_Features) + ',' + str(Origin) + ',' + str(Living_Status) + ',' + str(Reality) + ',' + str(Place_of_Birth) + ',' + str(Identity) + ',' + str(Citizenship) + ',' + str(Occupation) + ',' + str(Creator1) + ',' + str(Creator2) + ',' + str(First) + ',' + str(Blob))

#get all the output.txt files
path = os.path.join(os.getcwd(), "Scraped")
filenames = [f for f in os.listdir(path) if (os.path.isfile(os.path.join(path, f)) and 'output.txt'in os.path.join(path, f) and '_Vol_' not in os.path.join(os.getcwd(), f) and '(' in os.path.join(path, f))]


print(filenames)

#run the separator on each of the character files
original_stdout = sys.stdout
with open(os.path.join(os.getcwd(), "DataImport/DataImportFile.txt"), "a+") as f:
    sys.stdout = f
    for num, fileName in enumerate(filenames, start=0):
        if(fileName!= None): singleFileRead(os.path.join(path, fileName), fileName, num)   
sys.stdout =  original_stdout 


# In[ ]:



