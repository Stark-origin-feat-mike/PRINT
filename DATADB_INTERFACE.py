#!/Library/Python/2.7/site-packages
import MySQLdb
from enum import Enum

###########################################################################
#Execute mySQL command								 ####RELEVANT MYSQL####
#cursor.execute("SELECT * FROM STUDENTS")			 #### METHOD CALLS ####	
#													 ######################
#Iterate Selects														  #
#for row in cursor.fetchall():	// use fetchone() for first				  # 
#									result								  #
#	#print(row[0])														  #
#																		  #
#Query Construct Format													  #
#query = "INSERT INTO "+TABLES.STUDENTS+" VALUES (1, 'john doe')"		  #
###########################################################################


#TABLE STRING ENUMERATIONS
class TABLES(Enum):
	APPOINTMENTS = "appointments"
	CURATORS = "curators"
	CURATORSPACE ="curator_space"
	RESOURCE = "resource"
	SPACES = "spaces"
	STUDENTS = "students"
	STUDENTTRAINING ="student_training"
	TRAINING = "training"
	
class APPOINTMENT_ELEMENTS(Enum):
	ID ="id"
	STUDENTID="student_id"
	RESOURCEID="resource_id"
	STARTDATETIME="startdatetime"
	ENDDATETIME="enddatetime"
	
class CURATOR_ELEMENTS(Enum):
	ID="id"
	NAME="name"
	SPACEID="spaceid"
	
class CURATOR_SPACE_ELEMENTS(Enum):
	CURATORID="curatorid"
	SPACEID="spaceid"
	
class RESOURCE_ELEMENTS(Enum):
	ID="id"
	NAME="name"
	TRAININGREQUIRED="trainingrequired"
	SPACEID="spaceid"
	ACTIVE="active"
	TIME-LIMIT="time-limit"
	
class SPACES_ELEMENTS(Enum):
	ID="id"
	BUILDING="building"
	ROOM="room"
	NAME="name"
	
class STUDENTS_ELEMENTS(Enum):
	ID="ID"
	NAME="name"
	
class STUDENT_TRAINING_ELEMENTS(Enum):
	ID="ID"
	STUDENTID="studentid"
	TRAININGID="training_id"
class TRAINING_ELEMENTS(Enum):
	ID="id"
	RESOURCEID="resourceid"
	URL = "url"
	DESCRIPTION = "description"
	REQUIRED = "required"
	COMPLETED = "completed"

#MYSQL CONNECTION PARAMETERS
db = MySQLdb.connect(host="localhost",
						user="jwill124",
						passwd="ak47ppk",
						db="printdata")



def AllocateID(tablename, elementid, cur):
	id = 1
	query = "SELECT * FROM " + tablename +" ORDER BY " + str(elementid) + " DESC"
	cur.execute(query)
	row = cur.fetchone()
	if row is not None:
		id = (int(row[0]) + 1)
	return id
	
def DeleteTableEntryByProperty(tablename, tableproperty, entryname):
	query="DELETE FROM "+tablename+" WHERE "+tableproperty+" = '"+entryname+"'"
	print(query)
	cursor.execute(query)
	
	
def SelectAllFromTable(tablename):
	query="SELECT * FROM "+tablename
	cursor.execute(query)
	return cursor.fetchall()

def AddNewStudent(name):
	id = AllocateID(TABLES.STUDENTS, STUDENTS_ELEMENTS.ID, cursor)
	query = "INSERT INTO "+TABLES.STUDENTS+" VALUES ("+str(id)+",'"+name+"')"
	cursor.execute(query)
	db.commit()


def AddNewCurator(name):
	id = AllocateID(TABLES.CURATORS, CURATOR_ELEMENTS.ID,cursor)
	query = "INSERT INTO "+TABLES.CURATORS+" VALUES ("+str(id)+",'"+name+"')"
	cursor.execute(query)
	db.commit()

def AddNewSpace(building,room,name):
	id = AllocateID(TABLES.SPACES,SPACES_ELEMENTS.ID, cursor)
	query = "INSERT INTO "+TABLES.SPACES+" VALUES ("+str(id)+ ",'" +building+ "','" +room+"','" +name+"')"
	cursor.execute(query)
	
#TODO - TEST NEW FIELDS
def AddNewResource(name,trainingrequired,spacename, operational,timelimit):
	id = AllocateID(TABLES.RESOURCE,RESOURCE_ELEMENTS.ID,cursor)
	spaceid = 0
	query = "SELECT " + SPACES_ELEMENTS.ID + " FROM " + TABLES.SPACES + " WHERE " + SPACES_ELEMENTS.NAME + " = '" + spacename + "'" 
	cursor.execute(query)
	row = cursor.fetchone()
	if row is not None:
		spaceid = row[0]
	query = "INSERT INTO " + TABLES.RESOURCE + " VALUES (" +str(id)+ ",'" +name+ "','" +trainingrequired+ "'," +str(spaceid)+","+str(operational)+ ","+timelimit+")"
	cursor.execute(query)
	
def SetNewAppointment(studentid,resourceid,startdatetime,enddatetime):
	id = AllocateID(TABLES.APPOINTMENTS, APPOINTMENT_ELEMENTS.ID,cursor)
	query = "INSERT INTO " +TABLES.APPOINTMENTS+ " VALUES ("+str(id)+"," +str(studentid)+ "," +str(resourceid)+ ",'" +startdatetime+ "','" +enddatetime+ "')"
	cursor.execute(query)
	
#TODO - TEST ADDITIONS	
def RecordStudentTraining(studentid,trainingid,required,completed):
	query = "INSERT INTO "+TABLES.STUDENTTRAINING+" VALUES ("+str(studentid)+","+str(trainingid)+","+required+","+completed+")"
	cursor.execute(query)
	
def AddNewTraining(resourceid,url,description):
	id =  AllocateID(TABLES.TRAINING,TRAINING_ELEMENTS.ID,cursor)
	query="INSERT INTO "+TABLES.TRAINING+" VALUES ("+str(id)+","+str(resourceid)+",'"+url+"','"+description+"')"
	cursor.execute(query)
	
def AddCuratorToSpace(curatorid,spaceid):
	query="INSERT INTO "+TABLES.CURATORSPACE+ " VALUES ("+str(curatorid)+","+str(spaceid)+")"
	cursor.execute(query)
	
def RemoveSpaceByName(spacename):
	DeleteTableEntryByProperty(TABLES.SPACES, SPACES_ELEMENTS.NAME, spacename)

def RemoveResourceByName(resourcename):
	DeleteTableEntryByProperty(TABLES.RESOURCE,RESOURCE_ELEMENTS.NAME, resourcename)
	
#TODO - TEST
def RemoveCuratorFromSpaceByID(curatorid):
	DeleteTableEntryByProperty(TABLES.CURATORSPACE,CURATOR_SPACE_ELEMENTS.CURATORID,curatorid)

#TODO - TEST
def RemoveCuratorFromDatabase(curatorid):
	RemoveCuratorFromSpaceByID(curatorid)
	DeleteTableEntryByProperty(TABLES.CURATORS, CURATOR_ELEMENTS.ID, curatorid)

#TODO - TEST	
def RemoveStudentFromDatabase(studentid):
	DeleteTableEntryByProperty(TABLES.STUDENTS,STUDENTS_ELEMENTS.ID, studentid)
	
#TODO - TEST	
def RemoveTrainingFromDatabase(trainingid):
	DeleteTableEntryByProperty(TABLES.TRAINING, TRAINING_ELEMENTS.ID, trainingid)

#TODO - TEST
def RemoveAppointment(appointmentid):
	DeleteTableEntryByProperty(TABLES.APPOINTMENTS, APPOINTMENT_ELEMENTS.ID, appointmentid)
	
#TODO - TEST
def SetResourceStatus(resourceid,state):
	UpdateTableEntry(TABLES.RESOURCE, RESOURCE_ELEMENTS.STATUS, resourceid, state)
	
#TODO - TEST	
def UpdateTableEntry(table, tableproperty,itemid, value):
	query = "UPDATE "+ table + " SET " +tableproperty+" = "+value+" WHERE ID = " +itemid 
	cursor.execute(query)
	

cursor = db.cursor()


db.commit()
db.close()
