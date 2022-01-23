# This code is designed to output a paragraph that can be copied and pasted into a SQL insert statement


import sys

path = 'VolumeDataImportFile.txt'
write = open('parsedVolumes.txt', 'a')

with open(path, 'r') as read:
    for line in read:
        splitLine = line.split(',')
        id = splitLine[0]
        volumeName = splitLine[1].replace("_", " ")
        writers = splitLine[2]
        editors = splitLine[3]
        letterers = splitLine[4]
        penciler = splitLine[5]
        colorist = splitLine[6]
        inker = splitLine[7]
        Editor_In_Chief = splitLine[8]
        Cover_Artist = splitLine[9]
