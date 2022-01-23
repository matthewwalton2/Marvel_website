-- Input one line of data in order to test the php search functions
-- To run this:
-- source www/311-project/sqlScripts/testDataInput.sql

use mwalton2; 
CREATE TABLE Characters (CharID int, charName varchar(255), Gender varchar(255), eyeColor varchar(255));

INSERT INTO Characters VALUES
    (1413, 'Nicholas Fury', 'Male', 'Brown'),
    (2003, 'Adolf Hitler', 'Male', 'Brown')
    ;


--1413,Nicholas_Fury_(Earth-TRN852),United States GovernmentFormerlyHowling Commandos,Single,Male,,,,Brown,Eye-patch over his blind left eye,Human whose aging was slowed by the Infinity Formula,Deceased,Earth-TRN852,,No Dual,,Former President of the United States,Tim Seeley, Dan Jurgens,Death
--2003,Adolf_Hitler_(Earth-TRN852),Nazi Party,,Male,,,,Brown,,Human,Deceased,Earth-TRN852,,No Dual,,Dictator,Jason Aaron, Erica D'Urso,Death

-- use mwalton2; drop table Characters;