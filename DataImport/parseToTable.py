import sys

path = 'VolumeDataImportFiles.txt'
try {
    file = open(path, 'r')
}
catch {
    print("File " + path + " not found")
    quit()
}