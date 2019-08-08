import csv , json

csvFilePath = "./Courses.csv"
jsonFilePath = "./Courses.json"
TechTable_courses = []
def generate_tableJson():
	#read the csv and add the arr to a array
	with open (csvFilePath) as csvFile:
		csvReader = csv.DictReader(csvFile)
		for csvRow in csvReader:
			TechTable_courses.append(csvRow)
	for i in range(0,len(TechTable_courses)):
		TechTable_courses[i]['Course Name']+='#'
		TechTable_courses[i]['Course Name']+=TechTable_courses[i]['Link']

	# write the data to a json file
	with open(jsonFilePath, "w") as jsonFile:
		jsonFile.write('{"data": ')
		jsonFile.write(json.dumps(TechTable_courses, indent = 4))
		jsonFile.write("}")
generate_tableJson()