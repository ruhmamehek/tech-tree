import csv , json
import pandas as pd
csvFilePath = "./static/Courses.csv"
tableJsonFilePath = "./static/Courses.json"
graphJsonFilePath = "./static/graph.json"
color_list = ["128 0 0", "230 25 75", "255 255 25", "60 180 75", "70 240 240", "0 128 128", "0 130 200", "230 190 255", "245 130 48", "0 0 128", "240 50 230", "170 255 195", "128 128 0", "170 110 40"]
#clusters = {"BIO":1, "COM":2, "CSE":3, "DES":4, "ECE":5, "ECO":6, "ENG":7, "ENT":8, "ESC":9, "MGT":10, "MTH":11, "PSY":12, "SOC":13, "SSH":14}
l = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[]}
#https://sashat.me/2017/01/11/list-of-20-simple-distinct-colors/
#Maroon, Red, Yellow, Green, Cyan, Teal, Blue, Lavender, Orange, Navy, Magenta, Mint, Olive Brown
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
	node_params = '"borderColor": "250 240 44","text": "","textFont": "1|Arial|8|0|WINDOWS|1|-11|0|0|0|0|0|0|0|1|0|0|0|0|Arial","textColor": "0 0 0"'
	node_addn_params = '"group": "nodes","removed": false,"selected": false,"selectable": true,"locked": false,"grabbable": true,"pannable": false,"classes": ""'
	for node in range(0,len(names)-1):
		cluster = clusters[node]
		l[cluster].append(codes[node])
		nodes+='{"data":{"id":"'+codes[node]+'","height":"30","width":"30","clusterID":"'+str(cluster)+'","color":"'+color_list[cluster-1]+'","shape":"Rectangle",'+node_params+'},'+node_addn_params+'},'
	cluster = clusters[node+1]
	l[cluster].append(codes[node+1])
	nodes+='{"data":{"id":'+codes[node+1]+',"height":"30","width":"30","clusterID":"'+str(cluster)+'","color":"'+color_list[cluster-1]+'","shape":"Rectangle",'+node_params+'},'+node_addn_params+'}],'
	edges = '"edges":['
	edge_id = 0
	edge_params = '"text": "","textFont": "1|Arial|8|0|WINDOWS|1|-11|0|0|0|0|0|0|0|1|0|0|0|0|Arial","textColor": "0 0 0","style": "Solid","arrow": "None","width": "1"'
	edge_addn_params = '"group": "edges","removed": false,"selected": false,"selectable": true,"locked": false,"grabbable": true,"pannable": true,"classes": ""'
	for course in range(0,len(names)):
		for prereq in range(0, len(prerequisites[course])):
			if(prerequisites[course][prereq]!='None'):
				for code in range(0,len(codes)):
					if(prerequisites[course][prereq]==codes[code]):
						edge_id+=1
						edges+='{"data":{"id":"'+str(edge_id)+'","source":"'+codes[code]+'","target":"'+codes[course]+'","color":"0 0 0",'+edge_params+'},'+edge_addn_params+'},'
	edges = edges[:-1]
	edges+=']'
	graphJSON = '{'+nodes+edges+'}'
	print(graphJSON)
	with open(graphJsonFilePath, "w") as jsonFile:
		jsonFile.write(graphJSON)
		jsonFile.close()
generate_graphJson()