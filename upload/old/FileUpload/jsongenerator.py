import csv , json
import pandas as pd

csvFilePath = "./Courses.csv"
tableJsonFilePath = "./Courses.json"
graphJsonFilePath = "./graph.json"
TechTable_courses = []
TechTree_courses = []
def generate_tableJson():
	#read the csv and add the arr to a array
	with open (csvFilePath) as csvFile:
		csvReader = csv.DictReader(csvFile)
		for csvRow in csvReader:
			TechTable_courses.append(csvRow)
	for i in range(0,len(TechTable_courses)):
		TechTable_courses[i]['Course Name']+='#'
		TechTable_courses[i]['Course Name']+=TechTable_courses[i]['Link']
		TechTable_courses[i]['Prerequisites']=TechTable_courses[i]['Prerequisites'].replace('"','')
		TechTable_courses[i]['Preferable Prerequisites']=TechTable_courses[i]['Preferable Prerequisites'].replace('"','')
		TechTable_courses[i]['Antirequisites']=TechTable_courses[i]['Antirequisites'].replace('"','')
	# write the data to a json file
	with open(tableJsonFilePath, "w") as jsonFile:
		jsonFile.write('{"data": ')
		jsonFile.write(json.dumps(TechTable_courses, indent = 4))
		jsonFile.write("}")

def generate_graphJson():
	data = pd.read_csv(csvFilePath)
	data = data.to_dict()
	nodes = pd.DataFrame()
	name = []
	ID = []
	cluster = []
	names = data['Course Name']
	codes = data['Course Code']
	ids = data['Serial Number']
	clusters = data['cluster']
	for i in range(0,len(names)):
		name.append(codes[i]+":"+names[i])
		ID.append(ids[i])
		cluster.append(clusters[i])
	nodes['name']=name
	nodes['id']=ID
	nodes['cluster']=cluster
	print(nodes.head)
	nodes.to_json("./graph.json",orient='table')

	

generate_graphJson()
generate_tableJson()