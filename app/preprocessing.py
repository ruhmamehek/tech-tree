import csv
import pandas as pd
import re
import numpy

csvFilePath = "./static/Courses.csv"
data = pd.read_csv(csvFilePath) 

with open (csvFilePath) as csvFile:
	csvReader = csv.DictReader(csvFile)
	#check validity of course code
	for item in data["Course Code"]:
		if len(item)<3:
			print("Invalid Course Code", item)
		else:
			item=item.replace(" ", "")
			course_codes=list(item.split("/"))
			for cc in course_codes:
				if (cc[0].istitle() and cc[1].istitle() and cc[0].istitle())==False:
					print("First 3 letters should be capitalised ", cc)
	# #check validity of Semester
	# for item in data["Semester"]:
	# 	if item!="Monsoon" and item!="Winter" and item!="Summer":
	# 		print("Semester should be Monsoon/Summer/Winter, Semester ", item, " not allowed")
	# #check validity of Credits
	# for item in data["Credits"]:
	# 	if item!="1" and item!="2" and item!="4":
	# 		print("Credits should be 1/2/4, Credit ", item, " not allowed")

	#check validity of Prerequisites				
	for csvRow in csvReader:	
		stringreqd=csvRow["Prerequisites"]
		stringreqd=stringreqd.replace("or", ",") #splitting choice prereqs
		stringreqd=stringreqd.replace(" ", "")
		stringreqd=stringreqd.replace("\"", "")
		prereqs= list(stringreqd.split(","))

		ps=[]

		#checking if a course of given course code exists
		for item in prereqs:
			if item!='None' and len(item)!=0:
				if item not in data["Course Code"].values:
					print("Invalid Prerequisite, ", item)

		#checking multiple prerequisites are enclosed within inverted commass
		for item in prereqs:
			if prereqs.count(",")>0:
				if prereqs.count("\"")!=2:
					print("Multiple Prerequisites to be enclosed in double inverted commas")









