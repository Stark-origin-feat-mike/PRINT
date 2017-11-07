from DATADB_INTERFACE import *
from DATADB_INTERFACE import Database_INF as dbi

def TableAsXML(tablename):
	list = dbi.SelectAllFromTable(tablename)
	xml = "<"+tablename+">\n"
	entrytype = tablename[:-1]
	columnheader =TableFields(tablename)
	for i in range(0,len(list)):
		xml+="\t<"+entrytype+">\n"
		for j in range(0,len(list[i])):
			item = list[i][j]
			if not isinstance(item,str):
				item=str(item)
			xml+="\t\t<"+columnheader[j]+">\n"+"\t\t\t"+item+"\n"+"\t\t</"+columnheader[j]+">\n"
		xml+="\t</"+entrytype+">\n"
	xml+="<"+tablename+">"
	print(xml)
	
def TableFields(tablename):
	columnheader =[]
	if tablename == "appointments":
		for j in APPOINTMENT_ELEMENTS.FIELDS:
			columnheader.append(j)
		return(columnheader)
	if tablename == "curators":
		for j in CURATOR_ELEMENTS.FIELDS:
			columnheader.append(j)
		return(columnheader)
	if tablename == "curator_space":
		for j in CURATOR_SPACE_ELEMENTS.FIELDS:
			columnheader.append(j)
		return(columnheader)
	if tablename == "resource":
		for j in RESOURCE_ELEMENTS.FIELDS:
			columnheader.append(j)
		return(columnheader)
	if tablename == "spaces":
		for j in SPACES_ELEMENTS.FIELDS:
			columnheader.append(j)
		return(columnheader)
	if tablename == "students":
		for j in STUDENTS_ELEMENTS.FIELDS:
			columnheader.append(j)
		return(columnheader)
	if tablename == "student_training":
		for j in STUDENT_TRAINING_ELEMENTS.FIELDS:
			columnheader.append(j)
		return(columnheader)
	if tablename ==  "training":
		for j in TRAINING_ELEMENTS.FIELDS:
			columnheader.append(j)
		return(columnheader)
	return(columnheader)
	
