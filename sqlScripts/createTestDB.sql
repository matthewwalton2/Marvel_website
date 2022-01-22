-- This is a script that contains code to create (and delete) a test table in the mwalton2 database in MySQL
-- We don't have permission to create a database, so use the one with your ObieUsername
-- Run the first half to create the database, second half to delete it

-- to run this script in mySQL:
-- $ source www/311-project/sqlScripts/createTestDB.sql

-- This create a database testDB with one table (persons)
-- Each persons entity has an ID, Firstname, Lastname, and City
/*
use mwalton2; CREATE TABLE Persons (PersonID int, LastName varchar(255), FirstName varchar(255), City varchar(255));
INSERT INTO Persons VALUES
    (69, 'James', 'LeBron', 'Cleveland'),
    (3, 'Steph', 'Curry', 'San Francisco')
    ;
*/


-- This deletes everything in the table Persons, as if it never existed.
-- THIS CANNOT BE UNDONE
-- use mwalton2; drop table Persons;