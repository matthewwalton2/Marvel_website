-- Run this in mysql database mwalton2 to import all Characters data
LOAD DATA LOCAL INFILE '/usr/users/quota/students/2019/mwalton2/www/311-project/DataImport/DataImportFile.txt' INTO TABLE Characters FIELDS TERMINATED BY ',' LINES TERMINATED BY "\n" IGNORE 1 ROWS;