import csv , json
import pandas as pd
csvFilePath = "./static/Courses.csv"
tableJsonFilePath = "./static/Courses.json"
graphJsonFilePath = "./static/graph.json"
def generate_tableJson():
	TechTable_courses = []
	with open (csvFilePath) as csvFile:
		csvReader = csv.DictReader(csvFile)
		for csvRow in csvReader:
			course_code = list(csvRow["Course Code"].split("/"))[0]
			csvRow["Link"]="http://127.0.0.1:5000/viewDescription/filename?="+course_code
			TechTable_courses.append(csvRow)
	for i in range(0,len(TechTable_courses)):
		TechTable_courses[i]['Course Name']+='#'
		TechTable_courses[i]['Course Name']+=TechTable_courses[i]['Link']
		TechTable_courses[i]['Prerequisites']=TechTable_courses[i]['Prerequisites'].replace('"','')
		TechTable_courses[i]['Preferable Prerequisites']=TechTable_courses[i]['Preferable Prerequisites'].replace('"','')
		TechTable_courses[i]['Antirequisites']=TechTable_courses[i]['Antirequisites'].replace('"','')
	with open(tableJsonFilePath, "w") as jsonFile:
		jsonFile.write('{"data": ')
		jsonFile.write(json.dumps(TechTable_courses, indent = 4))
		jsonFile.write("}")
		jsonFile.close()
def generate_graphJson():
	data = pd.read_csv(csvFilePath)
	data = data.to_dict()
	nodes = pd.DataFrame()
	name = []
	ID = []
	cluster = []
	prereqs = []
	names = data['Course Name']
	codes = data['Course Code']
	ids = data['Serial Number']
	clusters = data['Cluster']
	prerequisites = data['Prerequisites']
	for entry in range(0,len(prerequisites)):
		if(isinstance(prerequisites[entry], float)):
			prerequisites[entry] = 'None'
		prerequisites[entry] = prerequisites[entry].replace("'","")
		prerequisites[entry] = prerequisites[entry].replace('"',"")
		prerequisites[entry] = prerequisites[entry].replace(" ", "")
		prerequisites[entry] = list(prerequisites[entry].split(","))
	for i in range(0,len(names)):
		name.append(codes[i]+":"+names[i])
		ID.append(ids[i])
		cluster.append(clusters[i])
		prereqs.append(prerequisites[i])
	nodes = '"nodes":['
	for node in range(0,len(names)-1):
		nodes+='{"data":{"id":"'+str(ID[node])+'","label":"'+codes[node]+'"}'+'},'
	nodes+='{"data":{"id":'+str(ID[node+1])+',"label":"'+codes[node+1]+'"}'+'}],'
	edges = '"edges":['
	for course in range(0,len(names)):
		for prereq in range(0, len(prerequisites[course])):
			if(prerequisites[course][prereq]!='None'):
				for code in range(0,len(codes)):
					if(prerequisites[course][prereq]==codes[code]):
						edges+='{"data":{"id":"'+str(code+1)+str(course+1)+'","source":"'+str(code+1)+'","target":"'+str(course+1)+'"}'+'},'
	edges = edges[:-1]
	edges+=']'
	graphJSON = '{'+nodes+edges+'}'
	with open(graphJsonFilePath, "w") as jsonFile:
		jsonFile.write(graphJSON)
		jsonFile.close()