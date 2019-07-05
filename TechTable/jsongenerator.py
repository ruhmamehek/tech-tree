import csv , json

csvFilePath = "./sampleCourses.csv"
jsonFilePath = "./sampleCourses.json"
arr = []

#read the csv and add the arr to a array
with open (csvFilePath) as csvFile:
	csvReader = csv.DictReader(csvFile)
	for csvRow in csvReader:
		arr.append(csvRow)

# write the data to a json file
with open(jsonFilePath, "w") as jsonFile:
	jsonFile.write('{"data": ')
	jsonFile.write(json.dumps(arr, indent = 4))
	jsonFile.write("}")

