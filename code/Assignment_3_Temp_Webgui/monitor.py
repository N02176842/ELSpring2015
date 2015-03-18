#!/usr/bin/env python


from datetime import datetime
import sqlite3 as mydb
import datetime
import os
import time
       

def main():

    # open the file that belongs to the temperature sensor
    tempfile = open("/sys/bus/w1/devices/28-000006574c70/w1_slave")

    tempfile_text = tempfile.read()
    tempfile.close()
    tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
    tempF = tempC*9.0/5.0+32.0

    # ENABLE Writing to html 
    print "Content-type: text/html\n\n"

    # Print on website the current temperature
    print "<h1> Current temperature is: " + str(tempC) + " C , " + str(tempF) + " F </h1>"

    con = None
    
    print  "<h1> BEGIN INSERTING data into templog.db </h1>"

    # connect to (/var/www/templog), we do this by CREATE an new sqlite3 'templog.db',
    # then, type the following on the Linxus terminal:
    # 'sudo cp templog.db /var/www/'
    # This will copy the original 'templog.db' that we have created, and paste it in 
    # '/var/www/' directory so we can use it and access it from the '/usr/lib/cgi-bin/monitor.py'
    con = mydb.connect('/var/www/templog.db')

    cur = con.cursor()
    # we create a variable 'now' and assign to it the current date and time
    now = datetime.datetime.now()

    # we insert both 'now' and 'tempC' into the table 'temps' inside 'templog.db'	    
    cur.execute("INSERT INTO temps VALUES(?,?)",(now,tempC))
    con.commit();
    con.close()

    print "<h1> Operation is Successful </h1>"
       

if __name__=="__main__":
    main()
