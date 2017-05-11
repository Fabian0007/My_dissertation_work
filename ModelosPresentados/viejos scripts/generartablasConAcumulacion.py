import os
import errno
import pandas as pd
import sys


def sorted(directory,numberTest, input):
	for i in range(0,numberTest):
		df = pd.read_csv(directory+'/test'+str(i)+'/'+input, delimiter=",",header=None)
		df.columns = ['id', 'pub']
		df_sort=df.sort_values(by='pub', axis=0,ascending=False)
		df_sort.to_csv(directory+'/test'+str(i)+'/testTables/'+'test'+input, sep=',', index=False, header=None)

def createTables(directory,numberTest, input):

	for i in range(0,numberTest):
		try:
			os.makedirs(directory+'/test'+str(i)+'/testTables')
		except OSError as exception:
			if exception.errno != errno.EEXIST:
				raise
		pub1 = open(directory+'/test'+str(i)+'/testTables/'+'pub1-'+input, 'w')
		ener = open(directory+'/test'+str(i)+'/testTables/'+'energy-'+input, 'w')
		aEner = open(directory+'/test'+str(i)+'/testTables/'+'agentsEnergy-'+input, 'w')
		prob1 = open(directory+'/test'+str(i)+'/testTables/'+'prob1-'+input, 'w')
		acumulatedPapers = open(directory+'/test'+str(i)+'/testTables/'+'acumulated-papers-'+input, 'w')
		actualPapers = open(directory+'/test'+str(i)+'/testTables/'+'actual-papers-'+input, 'w')
		pub2 = open(directory+'/test'+str(i)+'/testTables/'+'pub2-'+input, 'w')
		prob2 = open(directory+'/test'+str(i)+'/testTables/'+'prob2-'+input, 'w')
		pub3 = open(directory+'/test'+str(i)+'/testTables/'+'pub3-'+input, 'w')
		prob3 = open(directory+'/test'+str(i)+'/testTables/'+'prob3-'+input, 'w')
		entrada = open(directory+'/test'+str(i)+'/'+input,'r')
		linea=""
		tag=""
		active=False
		number=0
		for linea in entrada:
			if linea=='"x","y","color","pen down?"\n':
				active=True;
				continue                   
			if linea=='\n':
				if active:
					number=number+1;
					active=False;
			if active:
				if number==0:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub1.write(lineaNueva)
				if number==1:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					ener.write(lineaNueva)
				if number==2:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					aEner.write(lineaNueva)
				if number==3:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob1.write(lineaNueva)
				if number==4:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					acumulatedPapers.write(lineaNueva)
				if number==5:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					actualPapers.write(lineaNueva)
				if number==6:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub2.write(lineaNueva)
				if number==7:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob2.write(lineaNueva)
				if number==8:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub3.write(lineaNueva)
				if number==9:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob3.write(lineaNueva)
		entrada.close()
		pub1.close()
		ener.close()
		aEner.close()
		prob1.close()
		acumulatedPapers.close()
		actualPapers.close()
		pub2.close()
		prob2.close()
		pub3.close()
		prob3.close()

def getAverage(directory, numberTest, input):
	listOfNumbers=[]
	numberInformation=[]
	try:
		os.makedirs(directory+'/averageResults')
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
	for i in range(0,100):
		listOfNumbers.append(0)
		numberInformation.append(0)
	
	for i in range(0,numberTest):
		pub = open(directory+'/test'+str(i)+'/'+input, 'r')    	    	    
		numberLine=0
		for line in pub:
			line = line.replace("\n", '')
			listOfNumbers[numberLine]=listOfNumbers[numberLine]+int(line.split(',')[1])
			numberInformation[numberLine]=numberInformation[numberLine]+1
			numberLine=numberLine+1
		pub.close()

	pub = open(directory+'/averageResults/'+input, 'w') 

	for i in range(0,100):
		if numberInformation[i]!=0:
			pub.write(str(i)+','+str(listOfNumbers[i]/numberInformation[i])+'\n')
	pub.close()


def createJoin(directory, table1,table2, input):
	listOfNumbers=[]
	for i in range(0,3002):
		listOfNumbers.append(0)
	try:
		os.makedirs(directory+'/testTables/'+table1+'-'+table2)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
	tab1 = open(directory+'/testTables/'+table1+input, 'r')
	tab2 = open(directory+'/testTables/'+table2+input, 'r')
	entrada = open(directory+'/testTables/'+table1+'-'+table2+'/'+input,'w')
	i=0
	for line in tab1:
		listOfNumbers[i]=(line.split(',')[1])
		i=i+1
	i=0
	for line in tab2:
		entrada.write(listOfNumbers[i].replace("\n", '')+','+(line.split(',')[1]))
		i=i+1
	entrada.close()
	tab1.close()
	tab2.close()

def sortedTables():
	print "What is the directory?"
	directory = raw_input()
	print "How many test?"
	numberTest = int(raw_input())
	movement= ["1","100"]
	initialEnergy=["5","10","15"]
	probability1=["0.01", "0.1", "1"]
	probability2=["0.01", "0.1", "1"]
	file=""
	for i in initialEnergy:
		for j in movement:
			for l in probability1:
				for m in probability2:
					file=i+"-"+j+"-"+l+"-"+m+"-turtles.csv"
					sorted(directory,numberTest,file)


def joinTablesOld():
	print "What is the directory?"
	directory = raw_input()
	numberAgents = ["10000", "1000", "100"]
	movement = ["1"]
	initialProbability = ["0.01", "0.001", "1.0E-4"]
	probabilityIncrease = ["0.01", "0.001", "1.0E-4"]
	output = open(directory+'/averageResults/All.csv','w')
	for i in numberAgents:
		for j in movement:
			for l in initialProbability:
				for n in probabilityIncrease:
					data = open(directory+'/averageResults/'+i+"-"+j+"-"+l+"-"+n+"-turtles.csv")
					for line in data.xreadlines():
						output.write(line)
					data.close()
	output.close()

def getAverageOfTablesOld():
	print "What is the directory?"
	directory = raw_input()
	print "How many test?"
	numberTest = int(raw_input())
	numberAgents = ["100", "1000", "10000"]
	movement = ["1"]
	initialProbability = ["1.0E-4", "0.001", "0.01"]
	probabilityIncrease = ["1.0E-4", "0.001", "0.01"]
	file=""
	for i in numberAgents:
		for j in movement:
			for l in initialProbability:
				for n in probabilityIncrease:
					file=i+"-"+j+"-"+l+"-"+n+"-turtles.csv"
					getAverage(directory,numberTest,file)



def separateTablesOld():
	print "What is the directory?"
	directory = raw_input()
	print "How many test?"
	numberTest = int(raw_input())
	numberAgentsUniversity1 = ["10000", "1000"]
	numberAgentsUniversity2 = ["10000", "1000"]
	numberAgentsUniversity3 = ["10000", "1000"]
	initialProbability = ["0.1", "0.01"]
	probabilityIncrease1 = ["0.01", "1.0E-4"]
	probabilityIncrease2 = ["0.01", "1.0E-4", "1.0E-6"]
	probabilityIncrease3 = ["0.01", "1.0E-4", "1.0E-6"]
	initialProbabilityAgents = ["0.01", "1.0E-4", "1.0E-6"]
	initialEnergy = ["100"]

	file=""
	for i in numberAgentsUniversity1:
		for j in numberAgentsUniversity2:
			for l in numberAgentsUniversity3:
				for n in initialProbability:
					for m in probabilityIncrease1:
						for a in probabilityIncrease2:
							for b in probabilityIncrease3:
								for c in initialProbabilityAgents:
									for d in initialEnergy:
										file=i+"-"+j+"-"+l+"-"+n+"-"+m+"-"+a+"-"+b+"-"+c+"-"+d+"-curve.csv"
										createTables(directory,numberTest,file)
					



def calculatePublicationsOld():
	print "What is the directory?"
	directory = raw_input()
	movement= ["1","100"]
	initialEnergy=["5","10","15"]
	probability1=["0.01", "0.1", "1"]
	probability2=["0.01", "0.1", "1"]
	file=""
	for i in initialEnergy:
		for j in movement:
			for l in probability1:
				for m in probability2:
					file=i+"-"+j+"-"+l+"-"+m+"-curve.csv"
					calculatePublicationsForTable(directory,file)


def calculatePublicationsForTable(directory, input):
	tab = open(directory+'/testTables/publications'+input, 'r')
	new = open(directory+'/testTables/publicationsByTick'+input,'w')
	i=0
	beforeLine=0
	for line in tab:
		if line!="":
			newNumber=int(line.split(',')[1])-beforeLine
			new.write(str(i)+","+str(newNumber)+"\n")
			beforeLine=int(line.split(',')[1])
			i=i+1
	new.close()
	tab.close()

def separateTable():
	print "What is the directory?"
	directory = raw_input()
	numberTest = 1
	print "What is the name?"
	file = raw_input()
	createTables(directory,numberTest,file)

def getAverageOfTables():
	print "What is the directory?"
	directory = raw_input()
	print "How many test?"
	numberTest = int(raw_input())
	file = "test-curve.csv"
	getAverage(directory,numberTest,file)

def calculatePublications():
	print "What is the directory?"
	directory = raw_input()
	file = "test-curve.csv"
	calculatePublicationsForTable(directory,file)

def joinTables():
	print "What is the directory?"
	directory = raw_input()
	print "How many test?"
	numberTest = int(raw_input())
	file = "test-curve.csv"
	createJoin(directory,"energy", "publications", file)


def allOnOne():
	print "What is the directory?"
	directory = raw_input()
	print "How many test?"
	numberTest = int(raw_input())
	file = "100-100-1-curve.csv"
	createTables(directory,numberTest,file)
	#getAverage(directory,numberTest,file)
	#calculatePublicationsForTable(directory,file)
	#createJoin(directory,"energy", "publications", file)

def getAverageTurtles(directory, numberTest, input):
	listOfNumbers=[]
	numberInformation=[]
	try:
		os.makedirs(directory+'/testTables')
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
	for i in range(0,1000):
		listOfNumbers.append(0)
		numberInformation.append(0)
	
	for i in range(0,numberTest):
		pub = open(directory+'/test'+str(i)+'/testTables/'+'test'+input, 'r')    	    	    
		numberLine=0
		for line in pub:
			line = line.replace("\n", '')
			listOfNumbers[numberLine]=listOfNumbers[numberLine]+int(line.split(',')[1])
			numberInformation[numberLine]=numberInformation[numberLine]+1
			numberLine=numberLine+1
		pub.close()

	for i in range(0, len(listOfNumbers)):
		listOfNumbers[i]=(listOfNumbers[i]/numberInformation[i])

	values = []
	repitition = []
	j = 0
	isIn = False
	for number in listOfNumbers:
		if number not in values and number != 0:
			values.append(number)
			repitition.append(listOfNumbers.count(number))

	pub = open(directory+'/testTables/'+input, 'w') 

	for i in range(0, len(values)):
		pub.write(str(values[i])+','+str(repitition[i])+'\n')
	pub.close()


def getAverageOfTurtles():
	print "What is the directory?"
	directory = raw_input()
	print "How many test?"
	numberTest = int(raw_input())
	movement= ["1","100"]
	initialEnergy=["5","10","15"]
	probability1=["0.01", "0.1", "1"]
	probability2=["0.01", "0.1", "1"]
	file=""
	for i in initialEnergy:
		for j in movement:
			for l in probability1:
				for m in probability2:
					file=i+"-"+j+"-"+l+"-"+m+"-turtles.csv"
					sorted(directory,numberTest,file)
	for i in initialEnergy:
		for j in movement:
			for l in probability1:
				for m in probability2:
					file=i+"-"+j+"-"+l+"-"+m+"-turtles.csv"
					getAverageTurtles(directory,numberTest,file)

def generateProductivity():
	directory = 'ModeloSinAcumulacion'
	input = '10-1-1-turtles.csv'
	# df = pd.read_csv('ModelSinAcumulacion'+'/test0'+'/'+'15-100-1-turtles.csv', delimiter=",",header=None)
	# df.columns = ['id', 'pub', 'en', 'tick']
	# df_sort=df.sort_values(by='id', axis=0,ascending=False)
	# df_sort.to_csv('ModelSinAcumulacion'+'/test0'+'/'+'15-100-1-turtles.csv', sep=',', index=False, header=None)
	acumulado = open(directory+'/test0/'+input, 'r')
	linea=""
	tag=""
	active=False
	number=0
	agent=0
	salida = open(directory+'/test0/tables/'+str(agent)+input,'w');
	for linea in acumulado:
		if number == 0:
			salida = open(directory+'/test0/tables/'+str(agent)+'-'+input,'w')
			agent = agent +1
		salida.write(str(number)+','+linea.split(',')[1]+'\n')
		number = number + 1
		if(number == 10):
			number = 0
			salida.close()
	acumulado.close()



def menu():
	print "0. All on one"
	print "1. Separate into tables (old version)"
	print "2. Get average of tables (old version)"
	print "3. Calculate publications (old version)"
	print "4. Join tables (old version)"
	print "5. Get average agents productivity"
	print "6. Generate tables of university productivity"
	print "7. Separate one table"

	argument=input()
	switcher = {0: allOnOne, 1: separateTablesOld,2: getAverageOfTablesOld, 3: calculatePublicationsOld, 4: joinTablesOld, 5: getAverageOfTurtles, 6: generateProductivity, 7: separateTable}
	func = switcher.get(argument, lambda: "nothing")
	return func()

menu()
