-- Input one line of data in order to test the php search functions
-- To run this:
-- source www/311-project/sqlScripts/testDataInput.sql;



-- Living Status,Reality,Place of Birth,Identity,Citizenship,Occupation,Creator1,Creator2,First Appearance,All Tags
use mwalton2;
CREATE Table Characters (
    int Id,
    Name varchar(255),
    Affiliation varchar(255),
    Marital_status varchar(255),
    Gender varchar(255),
    Height varchar(255),
    Weight varchar(255),
    Eyes varchar(255),
    Hair varchar(255),
    Unusual_features varchar(255),
    Origin varchar(255),
    Living_status varchar(255),
    Reality varchar(255),
    Birthplace varchar(255),
    Identity varchar(255),
    Citizenship varchar(255),
    Occupation varchar(255),
    Creator1 varchar(255),
    Creator2 varchar(255),
    Premiere varchar(255),
    All_tags varchar(255)
);



-- This is for VOLUMES
--Id,Name,Writer,Editor,Letterer,Penciler,Colorist,Inker,Editor In Chief,Cover Artist,All Tags
use mwalton2;
CREATE Table Characters (
    int Id,
    Name varchar(255),
    Writer varchar(255),
    Editor varchar(255),
    Letterer varchar(255),
    Penciler varchar(255),
    Colorist varchar(255),
    Inker varchar(255),
    Editor_In_Chief varchar(255),
    Cover-Artist varchar(255),
    All_tags varchar(255)
);

/*
use mwalton2; 
CREATE TABLE Characters (CharID int, charName varchar(255), Gender varchar(255), eyeColor varchar(255));

INSERT INTO Characters VALUES
    (113, 'Ho Chi Minh', 'Male', ' '),
    (335, 'Professor Rex', 'Male', 'Brown'),
    (640, 'Norma Astrovik', 'Female', 'Brown'),
    (1413, 'Nicholas Fury', 'Male', 'Brown'),
    (1437, 'Peter Parker', 'Male', 'Hazel'),
    (2003, 'Adolf Hitler', 'Male', 'Brown')
    ;





--640,Norma_Astrovik_(Earth-616),,Widowed,Female,,,,Brown,,Human,Alive,Earth-616,,No Dual,,,Steve Gerber, Don Heck,Giant-Size Defenders #5,Characters|Female Characters|Humans (Homo sapiens)|No Dual Identity Characters|Steve Gerber/Creator|Don Heck/Creator|Widowed Characters|Brown Hair|Living Characters|Earth-616/Characters|Americans|1975 Character Debuts|Jewish Characters|Astrovik Family||
--335,Professor_Rex_(Earth-8311),X-Imals,Single,Male,,,Irises:Brown,No Hair At All,,Tyrannosaurus rex mutant,Alive,Earth-8311,,Secret,,Leader of X-Imals,Zeb Wells, Will Robson,Spider-Ham #2,Characters|X-Imals (Earth-8311)/Members|Male Characters|Tyrannosaurus rex|Dinosaurs|Secret Identity Characters|Zeb Wells/Creator|Will Robson/Creator|Single Characters|Brown Eyes|No Hair|Living Characters|Earth-8311/Characters|Leaders|2020 Character Debuts||
--113,Ho_Chi_Minh_(Earth-616),Vietnam,,Male,,,,,,Human,Alive,Earth-616,,No Dual,,Freedom fighter,Michael Hoskin, Anthony Flamini,Marvel Atlas #1,Characters|Male Characters|Humans (Homo sapiens)|No Dual Identity Characters|Michael Hoskin/Creator|Anthony Flamini/Creator|Stuart Vandal/Creator|Eric J. Moreels/Creator|Living Characters|Earth-616/Characters|Vietnamese|Leaders|2007 Character Debuts|Historical Figures|Vietnam War Characters||
--1437,Peter_Parker_(Earth-616), As Peter Parker:  Empire State University;formerly TNM,Single,Male,5′10″ (1.78 m),167 lbs (75.75 kg),Irises:Hazel,Brown,,Human mutate;Radioactive Spider bite during a science experiment endowed proportionate capabilities of an arachnid. A mugger he could have stopped went on to kill Uncle Ben.,Alive,Earth-616,Queens,Secret,,Adventurer,Stan Lee, Steve Ditko,Amazing Fantasy #15,Characters|Threats and Menaces (Earth-616)/Members|Daily Bugle (Front Line) (Earth-616)/Members|Uncle Ben Foundation (Earth-616)/Members|Parker Industries (Earth-616)/Members|Horizon Labs (Earth-616)/Members|Parker Technologies (Earth-11638)/Members|Daily Bugle (The DB!) (Earth-616)/Members|Daily Globe (Earth-616)/Members|Tricorp (Earth-616)/Members|Avengers (Earth-616)/Members|Kang Club (Multiverse)/Members|League of Realms (Earth-616)/Members|Spider-Army (Multiverse)/Members|Web-Warriors (Earth-001)/Members|Resistance (Earth-51838)/Members|Inklings (Earth-616)/Members|Avengers Unity Division (Earth-616)/Members|X-Men (Earth-616)/Members|Special Class (Earth-616)/Members|Mighty Avengers (Cage) (Earth-616)/Members|Future Foundation (Earth-616)/Members|Heroes for Hire (Knight & Wing) (Earth-616)/Members|New Avengers (Earth-616)/Members|Marvel Knights (Earth-616)/Members|Fantastic Four (Earth-616)/Members|Secret Avengers (Civil War) (Earth-616)/Members|Outlaws (Earth-616)/Members|New Fantastic Four (Earth-616)/Members|Brooklyn Avengers (Earth-616)/Members|Secret Defenders (Earth-616)/Members|Galactic Alliance of Spider-Men (Earth-616)/Members|Mighty (Earth-616)/Members|Spider Society (Earth-616)/Members|Frightful Four (Earth-616)/Members|Inner Demons (Earth-616)/Members|Triads (Earth-616)/Members|Male Characters|Mutates|Deities|Humans (Homo sapiens)|Secret Identity Characters|Stan Lee/Creator|Steve Ditko/Creator|Single Characters|Height 5 ft. 10 in. (1.78 m)|Weight 160-179 lbs (72.57-81.65 kg)|Hazel Eyes|Brown Hair|Living Characters|Earth-616/Characters|Americans|Body Guards|Inventors|Adventurers|Wrestlers|Vigilantes|Teachers|Students|Engineers|Mechanics|Scientists|1962 Character Debuts|Pages using Timeline|Outdated Fields/Character|Peter Parker (Earth-616)/Quotes|Power Grid Added|Power Grid/Intelligence/Gifted|Power Grid/Strength/Superhuman (800 lbs-25 ton)|Power Grid/Speed/Superhuman|Power Grid/Durability/Enhanced|Power Grid/Energy Projection/None|Power Grid/Fighting Skills/Experienced Fighter|Power Grid Complete|Twitter Users|Shared body characters|Regeneration|Superhuman Agility|Superhuman Stamina|Superhuman Reflexes|Superhuman Senses|Superhuman Strength|Wallcrawling|Energy Senses|Captain Universe|Web-Slinging|Leaping|Toxic Immunity|Precogs|Symbiotes-possessed|Human/Spider Hybrids|Hybrids|Parker Family|Doctors|Geneticists|Robotics|Chemists|Physicists|Formerly Deceased|Secret Wars (1984 Event) casualties|Former Vampires|Power Level 8|Doctor Octopus Experiment|Radioactive Spider-Powered|Spider-Verse participants|Reilly Family|Facebook Users|Consciousness Transferred|Time Travelers|The Other receptacles|Midtown High School Students|Gymnasts|Empire State University Student|Acrobats|Secret Wars (1984 Event) participants|Leaders|Armor Users|Trained by Captain America|Trained by Shang-Chi|Interdimensional Travelers|Multilingual|Martial Arts|Athletic Skills|Businesspeople|Shared Identities|Secret Wars (2015 Event) participants|Shared Identities: Successors|Millionaires|Magic-Based Mutates|Totemic Avatars|Social Network Users|Watson Family|Jean Grey School faculty|Floating Super-Hero Poker Game participants|Spider-Geddon participants|Gamma Ray Exposure|Strength Class 25|Magicians|Arthropod Form|Fighting Ability - Experienced fighter|Organic Webbing|Former Werewolves|Post-Traumatic Stress Disorder|Libra (Astrological Sign)|Atheist Characters||
--1413,Nicholas_Fury_(Earth-TRN852),United States GovernmentFormerlyHowling Commandos,Single,Male,,,,Brown,Eye-patch over his blind left eye,Human whose aging was slowed by the Infinity Formula,Deceased,Earth-TRN852,,No Dual,,Former President of the United States,Tim Seeley, Dan Jurgens,Death
--2003,Adolf_Hitler_(Earth-TRN852),Nazi Party,,Male,,,,Brown,,Human,Deceased,Earth-TRN852,,No Dual,,Dictator,Jason Aaron, Erica D'Urso,Death

-- use mwalton2; drop table Characters;