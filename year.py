#Convert CSV to JSON 
import re
import json
import csv

with open ("tags_list.csv" , "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"Publications": []}
    for row in reader:
        year = row[5]
        title = str(row[0])+" "+str(row[4]) #add tittle and source string together
        if(re.search("^.*2022.*$", title)):
            year = 2022
        elif(re.search("^.*2021.*$", title)):
            year = 2021
        elif(re.search("^.*2020.*$", title)):
            year = 2020
        elif(re.search("^.*2019.*$", title)):
            year = 2019
        elif(re.search("^.*2018.*$", title)):
            year = 2018
        elif(re.search("^.*2017.*$", title)):
            year = 2017
        elif(re.search("^.*2016.*$", title)):
            year = 2016
        elif(re.search("^.*2015.*$", title)):
            year = 2015
        elif(re.search("^.*2014.*$", title)):
            year = 2014
        elif(re.search("^.*2013.*$", title)):
            year = 2013
        elif(re.search("^.*2012.*$", title)):
            year = 2012
        elif(re.search("^.*2011.*$", title)):
            year = 2011
        elif(re.search("^.*2010.*$", title)):
            year = 2010
        elif(re.search("^.*2009.*$", title)):
            year = 2009
        elif(re.search("^.*2008.*$", title)):
            year = 2008
        elif(re.search("^.*2007.*$", title)):
            year = 2007
        elif(re.search("^.*2006.*$", title)):
            year = 2006
        elif(re.search("^.*2005.*$", title)):
            year = 2005
        elif(re.search("^.*2004.*$", title)):
        	year = 2004
        elif(re.search("^.*2003.*$", title)):
        	year = 2003
        elif(re.search("^.*2002.*$", title)):
        	year = 2002
        elif(re.search("^.*2001.*$", title)):
        	year = 2001
        elif(re.search("^.*2000.*$", title)):
        	year = 2000
        elif(re.search("^.*1999.*$", title)):
        	year = 1999
        elif(re.search("^.*1998.*$", title)):
        	year = 1998
        elif(re.search("^.*1997.*$", title)):
        	year = 1997
        elif(re.search("^.*1996.*$", title)):
        	year = 1996
        elif(re.search("^.*1995.*$", title)):
        	year = 1995
        elif(re.search("^.*1994.*$", title)):
        	year = 1994
        else:
            year = row[5]
        data["Publications"].append({"Title":row[0],"Authors":row[1],"Research Area":row[2],"Publication Type":row[3],"Source":row[4],"Year":year,"Link":row[6]})


with open ("data_json_format.json", "w") as f:
    json.dump(data, f, indent=4)


