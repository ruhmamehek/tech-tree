'''
import pandas as pd

df = pd.read_csv('sampleCourses.csv', dtype={
    "Course Name" : str,
    "Course Acronym" : str,
    "Course Code" : str,
    "Prerequisites" : str,
    "Antirequisites" : str,
    "Semester" : str,
    "Preferable Prerequisites" : str,
    "Professor" : str,
    "Credits" : str,
    "Link" : str
 })

#print(df)
Export = df.to_json (r'.\sampleCourses.json', orient='records')
'''
import csv , json

csvFilePath = "./TechTreeCourses.csv"
jsonFilePath = "./sampleCourses.json"
arr = []

#read the csv and add the arr to a array
with open (csvFilePath) as csvFile:
	csvReader = csv.DictReader(csvFile)
	for csvRow in csvReader:
		#print(csvRow)
		arr.append(csvRow)

# write the data to a json file
with open(jsonFilePath, "w") as jsonFile:
	jsonFile.write('{"data": ')
	jsonFile.write(json.dumps(arr, indent = 4))
	jsonFile.write("}")