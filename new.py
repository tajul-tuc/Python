#Convert CSV to JSON 
import json
import csv

with open ("bibliothek_data.csv" , "r",encoding='utf-8') as f:
	reader = csv.reader(f)
	next(reader)
	data = {"publicstions": []}
	for row in reader:
		# print(row[0])
		# print(row[1])
		# print(row[2])
		# print(row[2])
		# print(row[3])
		# print(row[4])
		# print(row[5])
 		data["publicstions"].append({"Title":row[0],"Authors":row[1],"Research Area":row[2],"Publication Type":row[3],"Source":row[4],"Year":row[5],"Link":row[6]})


with open ("final.json", "w") as f:
	json.dump(data, f, indent=4)
