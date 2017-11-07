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
	MARKERS = "markers"
	
class MARKERS_ELEMENTS(Enum):
	FIELDS = ['id','name','address','lat','lng','type']
	ID = "id"
	NAME = "name"
	ADDRESS = "address"
	LAT = "lat"
	LNG = "lng"
	TYPE = "type"
	
class APPOINTMENT_ELEMENTS(Enum):
	FIELDS=['id','student_id','resource_id','startdatetime','enddatetime']
	ID ="id"
	STUDENTID="student_id"
	RESOURCEID="resource_id"
	STARTDATETIME="startdatetime"
	ENDDATETIME="enddatetime"
	
class CURATOR_ELEMENTS(Enum):
	FIELDS=['id','name','spaceid','email']
	ID="id"
	NAME="name"
	SPACEID="spaceid"
	EMAIL="email"
	
class CURATOR_SPACE_ELEMENTS(Enum):
	FIELDS=['curatorid','spaceid']
	CURATORID="curatorid"
	SPACEID="spaceid"
	
class RESOURCE_ELEMENTS(Enum):
	FIELDS=['id','name','trainingrequired','spaceid','operational','time_limit']
	ID="id"
	NAME="name"
	TRAININGREQUIRED="trainingrequired"
	SPACEID="spaceid"
	OPERATIONAL="operational"
	TIME_LIMIT="time-limit"
	
class SPACES_ELEMENTS(Enum):
	FIELDS=['id','building','room','name']
	ID="id"
	BUILDING="building"
	ROOM="room"
	NAME="name"
	
class STUDENTS_ELEMENTS(Enum):
	FIELDS=['ID','name']
	ID="ID"
	NAME="name"
	
class STUDENT_TRAINING_ELEMENTS(Enum):
	FIELDS=['ID','studentid','training_id']
	ID="ID"
	STUDENTID="studentid"
	TRAININGID="training_id"
	
class TRAINING_ELEMENTS(Enum):
	FIELDS=['id','resourceid','url','description','required','completed']
	ID="id"
	RESOURCEID="resourceid"
	URL = "url"
	DESCRIPTION = "description"
	REQUIRED = "required"
	COMPLETED = "completed"

	
db = MySQLdb.connect(host="localhost",
							user="jwill124",
							passwd="ak47ppk",
							db="printdata")
		
cursor = db.cursor()


class Database_INF:
		

	@staticmethod
	def AllocateID(tablename, elementid):
		id = 1
		query = "SELECT * FROM " + tablename +" ORDER BY " + str(elementid) + " DESC"
		cursor.execute(query)
		row = cursor.fetchone()
		if row is not None:
			id = (int(row[0]) + 1)
		return id
	
	@staticmethod
	def DeleteTableEntryByProperty(tablename, tableproperty, entry):
		if not isinstance(entry,str):
			entry = str(entry)
		query="DELETE FROM "+tablename+" WHERE "+tableproperty+" = '"+entry+"'"
		print(query)
		cursor.execute(query)
		db.commit()
		
	@staticmethod
	def SelectAllFromTable(tablename):
		query="SELECT * FROM "+tablename
		cursor.execute(query)
		return cursor.fetchall()

	@staticmethod
	def AddNewStudent(name):
		id = Database_INF.AllocateID(TABLES.STUDENTS, STUDENTS_ELEMENTS.ID)
		query = "INSERT INTO "+TABLES.STUDENTS+" VALUES ("+str(id)+",'"+name+"')"
		cursor.execute(query)
		db.commit()

	@staticmethod
	def AddNewCurator(name,email):
		id = Database_INF.AllocateID(TABLES.CURATORS, CURATOR_ELEMENTS.ID)
		query = "INSERT INTO "+TABLES.CURATORS+" VALUES ("+str(id)+",'"+name+"','"+email+"')"
		cursor.execute(query)
		db.commit()

	@staticmethod
	def AddNewSpace(building,room,name):
		id = Database_INF.AllocateID(TABLES.SPACES,SPACES_ELEMENTS.ID)
		query = "INSERT INTO "+TABLES.SPACES+" VALUES ("+str(id)+ ",'" +building+ "','" +room+"','" +name+"')"
		cursor.execute(query)
		db.commit()
		
	@staticmethod
	def AddNewResource(name,trainingrequired,spaceid, operational,timelimit):
		id = Database_INF.AllocateID(TABLES.RESOURCE,RESOURCE_ELEMENTS.ID)
		query = "INSERT INTO " + TABLES.RESOURCE + " VALUES (" +str(id)+ ",'" +name+ "','" +trainingrequired+ "'," +str(spaceid)+","+str(operational)+ ",'"+timelimit+"')"
		print(query)
		cursor.execute(query)
		db.commit()
	
	@staticmethod
	def SetNewAppointment(studentid,resourceid,startdatetime,enddatetime):
		id = Database_INF.AllocateID(TABLES.APPOINTMENTS, APPOINTMENT_ELEMENTS.ID)
		query = "INSERT INTO " +TABLES.APPOINTMENTS+ " VALUES ("+str(id)+"," +str(studentid)+ "," +str(resourceid)+ ",'" +startdatetime+ "','" +enddatetime+ "')"
		cursor.execute(query)
		db.commit()
		
	@staticmethod
	def RecordStudentTraining(studentid,trainingid,required,completed):
		query = "INSERT INTO "+TABLES.STUDENTTRAINING+" VALUES ("+str(studentid)+","+str(trainingid)+","+str(required)+","+str(completed)+")"
		cursor.execute(query)
		db.commit()
		
	@staticmethod
	def AddNewTraining(resourceid,url,description):
		id =  Database_INF.AllocateID(TABLES.TRAINING,TRAINING_ELEMENTS.ID)
		query="INSERT INTO "+TABLES.TRAINING+" VALUES ("+str(id)+","+str(resourceid)+",'"+url+"','"+description+"')"
		cursor.execute(query)
		db.commit()
		
	@staticmethod
	def AddCuratorToSpace(curatorid,spaceid):
		query="INSERT INTO "+TABLES.CURATORSPACE+ " VALUES ("+str(curatorid)+","+str(spaceid)+")"
		cursor.execute(query)
		db.commit()
		
	@staticmethod
	def RemoveSpaceByName(spacename):
		Database_INF.DeleteTableEntryByProperty(TABLES.SPACES, SPACES_ELEMENTS.NAME, spacename)
		db.commit()

	@staticmethod
	def RemoveResourceByName(resourcename):
		Database_INF.DeleteTableEntryByProperty(TABLES.RESOURCE,RESOURCE_ELEMENTS.NAME, resourcename)
		db.commit()
		
	
	@staticmethod
	def RemoveCuratorFromSpaceByID(curatorid):
		Database_INF.DeleteTableEntryByProperty(TABLES.CURATORSPACE,CURATOR_SPACE_ELEMENTS.CURATORID,curatorid)
		db.commit()


	@staticmethod
	def RemoveCuratorFromDatabase(curatorid):
		Database_INF.RemoveCuratorFromSpaceByID(curatorid)
		Database_INF.DeleteTableEntryByProperty(TABLES.CURATORS, CURATOR_ELEMENTS.ID, curatorid)
		db.commit()

	
	@staticmethod	
	def RemoveStudentFromDatabase(studentid):
		Database_INF.DeleteTableEntryByProperty(TABLES.STUDENTS,STUDENTS_ELEMENTS.ID, studentid)
		db.commit()
		
	@staticmethod
	def RemoveTrainingFromDatabase(trainingid):
		Database_INF.DeleteTableEntryByProperty(TABLES.TRAINING, TRAINING_ELEMENTS.ID, trainingid)
		db.commit()

	
	@staticmethod
	def RemoveAppointment(appointmentid):
		Database_INF.DeleteTableEntryByProperty(TABLES.APPOINTMENTS, APPOINTMENT_ELEMENTS.ID, appointmentid)
		db.commit()
		
	
	@staticmethod
	def SetResourceStatus(resourceid,state):
		Database_INF.UpdateTableEntry(TABLES.RESOURCE, RESOURCE_ELEMENTS.OPERATIONAL, resourceid, state)
		db.commit()
		
	
	@staticmethod	
	def UpdateTableEntry(table, tableproperty,itemid, value):
		if not isinstance(value,str):
			value = str(value)
		query = "UPDATE "+ table + " SET " +tableproperty+" = "+value+" WHERE ID = " +str(itemid) 
		cursor.execute(query)
		db.commit()

		
