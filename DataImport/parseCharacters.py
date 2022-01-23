# This code is designed to output a paragraph that can be copied and pasted into a SQL insert statement


import sys

path = 'DataImportFile.txt'

with open(path, 'r') as read:
    for line in read:
        # Initialize variables
        Id = 0
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
        Blob = ‘’

        arr = line.split(',')
        id = arr[0]
        try: 
            name = arr[1].rpartition('(')[0].replace('_', ' ')
            planet = arr[1].rpartition('(')[2].split(')')[0]
            affiliation = arr[2]
            marriage = arr[3]
            gender = arr[4]
        except:
            pass 
        


Id = 0
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
Blob = ‘’
Its still big enough that git is complaining