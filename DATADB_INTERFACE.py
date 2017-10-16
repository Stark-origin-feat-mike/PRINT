#!/Library/Python/2.7/site-packages
import MySQLdb
from enum import Enum

###########################################################################
#Execute mySQL command								 ####RELEVANT MYSQL####
#cursor.execute("SELECT * FROM STUDENTS")			 #### METHOD CALLS ####	
#													 ######################
#Iterate Selects														  #
#for row in cursor.fetchall():	// use fetchone() for first				  # #									result								  #
#	#print(row[0])														  #
#																		  #
#Query Construct Format													  #
#query = "INSERT INTO "+TABLES.STUDENTS+" VALUES (1, 'john doe')"		  #
###########################################################################

class TABLES(Enum):
	APPOINTMENT = "appointments"
	CURATORS = "curators"
	CURATORSPACE ="curator_space"
	RESOURCE = "resource"
	SPACE = "spaces"
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
	
class SPACES_ELEMENTS(Enum):
	ID="id"
	BUILDING="building"
	ROOM="room"
	
class STUDENTS_ELEMENTS(Enum):
	ID="ID"
	NAME="name"
	
class STUDENT_TRAINING_ELEMENTS(Enum):
	STUDENTID="studentid"
	TRAININGID="training_id"
class TRAINING(Enum):
	ID="id"
	RESOURCEID="resourceid"


db = MySQLdb.connect(host="localhost",
						user="jwill124",
						passwd="ak47ppk",
						db="printdata")

cursor = db.cursor()


def CreateNewStudent(name):
	#TODO - MOVE ID ALLOC TO NEW METHOD
	id = 1
	query="SELECT * FROM "+TABLES.STUDENTS+ " ORDER BY " + str(STUDENTS_ELEMENTS.ID) + " DESC"
	cursor.execute(query)
	row=cursor.fetchone()
	if row is not None:
		id=int(row[0])+1
	#id = AllocateID(TABLES.STUDENTS, STUDENT_ELEMENTS.ID)
	query = "INSERT INTO "+TABLES.STUDENTS+" VALUES ("+str(id)+",'"+name+"')"
	cursor.execute(query)
	db.commit()

#TODO - TEST	
def CreateNewCurator(name,spacename):
	#TODO - MOVE ID ALLOC TO NEW METHOD
	id = 1
	spaceid = 1
	cursor.execute("SELECT * FROM "+TABLES.CURATORS+ " ORDER BY " + str(CURATOR_ELEMENTS.ID) + " DESC LIMIT 0,1")
	row=cursor.fetchone()
	if row is not None:
		id=row[0]
	#id = AllocateID(TABLES.CURATORS, CURATOR_ELEMENTS.ID)
	
	#TODO - FETCH SPACE ID FOR GIVEN SPACE	
	#query= "SELECT " +SPACES_ELEMENTS.ID+ " WHERE " + SPACES_ELEMENTS.NAME + " = " + spacename
	#cursor.execute(query)	
	#row=curesor.fetchone()
	#if row is not Noone:
	#	spaceid=row[0]
	
	query = "INSERT INTO "+TABLES.CURATORS+" VALUES ("+str(id)+",'"+name+"')"
	
	#TEST
	print(query)
	
	cursor.execute(query)
	db.commit()


#TODO ADDSPACE()
#TODO ADDRESOURCE()
#TODO SETAPPOINTMENT()
#TODO RECORDSTUDENTTRAINING()
#TODO ADDTRAINING()
#TODO ADDCURATORTOSPACE()***SEE CURATOR_SPACE LAYOUT***
#TODO REMOVESPACE()
#TODO REMOVERESOURCE()
#TODO REMOVECURATORFROMSPACE()
#TODO REMOVECURATORFROMDATABASE()
#TODO REMOVESTUDENTFROMDATABASE()
#TODO REMOVESTUDENTTRAINING()
#TODO CANCELAPPOINTMENT()

	
db.commit()
db.close()