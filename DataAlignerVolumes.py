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
    Writer = ''
    Editor = ''
    Letterer = ''
    Penciler = ''
    Colorist = ''
    Inker = ''
    Editor_In_Chief = ''
    Cover_Artist = ''
    
    
    
    #blob is a big mess of tags that are haphazardly added to each page on the marvel wiki, anything from duplicates of the above to their powers to any of the creators or their favorite food
    Blob = ''
    
    Name = name.split("_output.txt")[0]
    #get character name from the input file
    
     #open the input file and break up by tabs then commas, as done by the 
    with open(fileName,'r') as tsvin:
        for line in csv.reader(tsvin, delimiter='\t'):
            for categories in csv.reader(line, delimiter = ','):
                try:
                    if(not categories):
                        continue
                    #if we see the telltale sign of a blob, start adding to it
                    elif(categories[0] == "Comics" or categories[1] == "Comics" or categories[2] == "Comics"):
                        #The Marvel wiki is not consistent as to where this tag appears
                        for item in categories:
                            if ('/Cover Artist' in item):
                                Cover_Artist += item.split('/')[0] + ' '
                            if ('/Writer' in item):
                                Writer += item.split('/')[0] + ' '
                            if ('/Editor' in item):
                                Editor += item.split('/')[0] + ' '
                            if ('/Letterer' in item):
                                Letterer += item.split('/')[0] + ' '
                            if ('/Penciler' in item):
                                Penciler += item.split('/')[0] + ' '
                            if ('/Colorist' in item):
                                Colorist += item.split('/')[0] + ' '
                            if ('/Inker' in item):
                                Inker += item.split('/')[0] + ' '
                            if ('/Editor-in-Chief' in item):
                                Editor_In_Chief += item.split('/')[0] + ' '
                            Blob += item
                            Blob += '|'
                        break
                    else:
                        return
                except IndexError:
                    continue
    print(str(id) + ',' + str(Name) + ',' + str(Writer) + ',' + str(Editor) + ',' + str(Letterer) + ',' + str(Penciler) + ',' + str(Colorist) + ',' + str(Inker) + ',' + str(Editor_In_Chief) + ',' + str(Cover_Artist) + ',' + str(Blob))
                
        
#get all the output.txt files
path = os.path.join(os.getcwd(), "Scraped")
filenames = [f for f in os.listdir(path) if (os.path.isfile(os.path.join(path, f)) and 'output.txt'in os.path.join(path, f) and '_Vol_' in os.path.join(os.getcwd(), f))]


print(filenames)

#run the separator on each of the character files
original_stdout = sys.stdout
with open(os.path.join(os.getcwd(), "DataImport/VolumeDataImportFile.txt"), "a+") as f:
    sys.stdout = f
    for num, fileName in enumerate(filenames, start=0):
        if(fileName!= None): singleFileRead(os.path.join(path, fileName), fileName, num)   
sys.stdout =  original_stdout 


# In[ ]:




