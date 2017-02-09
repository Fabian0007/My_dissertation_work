import os
import errno

def createTables(directory,numberTest, input):

	for i in range(0,numberTest):
		try:
			os.makedirs(directory+'/test'+str(i)+'/testTables')
		except OSError as exception:
			if exception.errno != errno.EEXIST:
				raise
		pub = open(directory+'/test'+str(i)+'/testTables/'+'publications'+input, 'w')
		ener = open(directory+'/test'+str(i)+'/testTables/'+'energy'+input, 'w')
		aEner = open(directory+'/test'+str(i)+'/testTables/'+'agentsEnergy'+input, 'w')
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
					pub.write(lineaNueva)
				if number==1:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					ener.write(lineaNueva)
				if number==2:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					aEner.write(lineaNueva)
		entrada.close()
		pub.close()
		ener.close()
		aEner.close()



def getAverage(directory, numberTest, input):
	listOfNumbers=[]
	numberInformation=[]
	try:
		os.makedirs(directory+'/testTables')
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
	for i in range(0,3002):
		listOfNumbers.append(0)
		numberInformation.append(0)
	
	for i in range(0,numberTest):
		pub = open(directory+'/test'+str(i)+'/testTables/'+'publications'+input, 'r')    	    	    
		numberLine=0
		for line in pub:
			line = line.replace("\n", '')
			listOfNumbers[numberLine]=listOfNumbers[numberLine]+int(line.split(',')[1])
			numberInformation[numberLine]=numberInformation[numberLine]+1
			numberLine=numberLine+1
		pub.close()

	pub = open(directory+'/testTables/'+'publications'+input, 'w') 

	for i in range(0,3002):
		if numberInformation[i]!=0:
			pub.write(str(i)+','+str(listOfNumbers[i]/numberInformation[i])+'\n')
	pub.close()

	listOfNumbers=[]
	numberInformation=[]
	for i in range(0,3002):
		listOfNumbers.append(0)
		numberInformation.append(0)
	
	for i in range(0,numberTest):
		pub = open(directory+'/test'+str(i)+'/testTables/'+'agentsEnergy'+input, 'r')    	    	    
		numberLine=0
		for line in pub:
			line = line.replace("\n", '')
			listOfNumbers[numberLine]=listOfNumbers[numberLine]+int(line.split(',')[1])
			numberInformation[numberLine]=numberInformation[numberLine]+1
			numberLine=numberLine+1
		pub.close()

	pub = open(directory+'/testTables/'+'agentsEnergy'+input, 'w') 

	for i in range(0,3002):
		if numberInformation[i]!=0:
			pub.write(str(i)+','+str(listOfNumbers[i]/numberInformation[i])+'\n')
	pub.close()


	listOfNumbers=[]
	numberInformation=[]
	for i in range(0,3002):
		listOfNumbers.append(0)
		numberInformation.append(0)
	
	for i in range(0,numberTest):
		pub = open(directory+'/test'+str(i)+'/testTables/'+'energy'+input, 'r')    	    	    
		numberLine=0
		for line in pub:
			line = line.replace("\n", '')
			listOfNumbers[numberLine]=listOfNumbers[numberLine]+float(line.split(',')[1])
			numberInformation[numberLine]=numberInformation[numberLine]+1
			numberLine=numberLine+1
		pub.close()

	pub = open(directory+'/testTables/'+'energy'+input, 'w') 

	for i in range(0,3002):
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


def joinTablesOld():
	print "What is the directory?"
	directory = raw_input()
	print "table 1?"
	table1 = raw_input()
	print "table 2?"
	table2 = raw_input()
	growth_rate_papers= ["0.01","1","10"]
	universities=["10","100","1000"]
	energy_initial=["10","100","1000"]
	file=""
	for i in universities:
		for j in energy_initial:
			for l in growth_rate_papers:
				file=i+"-"+j+"-"+l+"-curve.csv"
				createJoin(directory,table1, table2, file)

def getAverageOfTablesOld():
	print "What is the directory?"
	directory = raw_input()
	print "How many test?"
	numberTest = int(raw_input())
	growth_rate_papers= ["0.01","1","10"]
	universities=["10","100","1000"]
	energy_initial=["10","100","1000"]
	file=""
	for i in universities:
		for j in energy_initial:
			for l in growth_rate_papers:
				file=i+"-"+j+"-"+l+"-curve.csv"
				getAverage(directory, numberTest, file)



def separateTablesOld():
	print "What is the directory?"
	directory = raw_input()
	print "How many test?"
	numberTest = int(raw_input())
	growth_rate_papers= ["0.01","1","10"]
	universities=["10","100","1000"]
	energy_initial=["10","100","1000"]
	file=""
	for i in universities:
		for j in energy_initial:
			for l in growth_rate_papers:
				file=i+"-"+j+"-"+l+"-curve.csv"
				createTables(directory,numberTest,file)



def calculatePublicationsOld():
	print "What is the directory?"
	directory = input()
	growth_rate_papers= ["0.01","1","10"]
	universities=["10","100","1000"]
	energy_initial=["10","100","1000"]
	file=""
	for i in universities:
		for j in energy_initial:
			for l in growth_rate_papers:
				file=i+"-"+j+"-"+l+"-curve.csv"
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
	print "How many test?"
	numberTest = int(raw_input())
	file = "test-curve.csv"
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
	file = "test-curve.csv"
	createTables(directory,numberTest,file)
	getAverage(directory,numberTest,file)
	calculatePublicationsForTable(directory,file)
	createJoin(directory,"energy", "publications", file)

def menu():
	print "0. All on one"
	print "1. Separate into tables (old version)"
	print "2. Get average of tables (old version)"
	print "3. Calculate publications (old version)"
	print "4. Join tables (old version)"

	argument=input()
	switcher = {0: allOnOne, 1: separateTablesOld,2: getAverageOfTablesOld, 3: calculatePublicationsOld, 4: joinTablesOld}
	func = switcher.get(argument, lambda: "nothing")
	return func()

menu()