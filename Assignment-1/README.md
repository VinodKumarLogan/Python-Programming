Assignment 1 
=============

#####usage: 
                 -------
                 wikidb.py  [-h] [-i --insert] [-u --update] [-d --delete]

                 [-f --filename] [-g --generate] [-s --select] [--interactive]

optional arguments:
--------------------
  -h, --help     show this help message and exit
  
  -i --insert    Insert entries into the database
  
  -u --update    Update the entries in the database
  
  -d --delete    Delete an entry in database
  
  -f --filename  Filename which contains the database
  
  -g --generate  Generates the random entries for the database
  
  -s --select    Select particular entries from database
  
  --interactive  Run in interactive mode

Syntax :
===========
#####Select  : 
        
                    <field(s) to be selected> where 
                    condition(1) and/or condition(2) and/or 
                    condition(3) ... condition(n).
                    Here "and" has higher precedence than "
                 
         
#####Insert : 
      
                    field(1)=value(1),field(2)=value(2)...field(n)=value(n);
         
         
#####Update :
        
                     <field(s) to be updated> where condition(1) 
                     and/or condition(2) and/or condition(3) ... condition(n)
#####Delete :
         
                      where condition(1) and/or condition(2) and/or 
                      condition(3)... condition(n)'''
                      
                      
#####Create :
       
                      Read from existing db file and create 
                      the database.Also create database using 
                      random entries.If the file you specify already exists 
                      the new entries will be appended to the file and 
                      original entries will be unchanged.If random entry generatation 
                      option is not used then the database will be created using 
                      the entries present in the file
