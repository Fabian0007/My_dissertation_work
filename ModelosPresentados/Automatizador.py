import os
import errno
import pandas as pd
import sys


def menu():
	print "1. Modelo sin competencia"
	print "2. Modelo con competencia"
	argumento = input()
	directorio = ""
	if(argumento == 1):
		directorio = "SinCompetencia"
	else:
		directorio = "ConCompetencia"

	print "1. Separar un resultado en tablas"
	print "2. Generar el promedio de las tablas de resultado"
	print "3. Unir tablas"
	print "4. Generar el promedio de productividad de los agentes"
	argumento = input()
	switcher = {1: separarResultado(directorio),2: obtenerPromedioResultado(directorio), 3: unirResultados(directorio), 4: generarPromedioProductividad(directorio)}
	func = switcher.get(argumento, lambda: "nothing")
	return func()

#Separa un resultado de la simulacion, en las tablas correspondientes 
def separarResultado(directorio):
	numeroPruebas= 1
	print "What is the name?"
	archivo = raw_input()
	if directorio == "SinCompetencia":
		crearTablasSinCompetencia(directorio, numeroPruebas, archivo)
	else:
		crearTablasConCompetencia(directorio, numeroPruebas, archivo)

#Genera las tablas a partir del resultado de una simulacion para el modelo sin competencia
def crearTablasSinCompetencia(directorio,numeroPruebas, archivo):

	for i in range(0,numeroPruebas):
		try:
			os.makedirs(directorio+'/test'+str(i)+'/testTables')
		except OSError as exception:
			if exception.errno != errno.EEXIST:
				raise
		pub1 = open(directorio+'/test'+str(i)+'/testTables/'+'pub1-'+archivo, 'w')
		ener = open(directorio+'/test'+str(i)+'/testTables/'+'energy-'+archivo, 'w')
		aEner = open(directorio+'/test'+str(i)+'/testTables/'+'agentsEnergy-'+archivo, 'w')
		prob1 = open(directorio+'/test'+str(i)+'/testTables/'+'prob1-'+archivo, 'w')
		acumulatedPapers = open(directorio+'/test'+str(i)+'/testTables/'+'acumulated-papers-'+archivo, 'w')
		actualPapers = open(directorio+'/test'+str(i)+'/testTables/'+'actual-papers-'+archivo, 'w')
		pub2 = open(directorio+'/test'+str(i)+'/testTables/'+'pub2-'+archivo, 'w')
		prob2 = open(directorio+'/test'+str(i)+'/testTables/'+'prob2-'+archivo, 'w')
		pub3 = open(directorio+'/test'+str(i)+'/testTables/'+'pub3-'+archivo, 'w')
		prob3 = open(directorio+'/test'+str(i)+'/testTables/'+'prob3-'+archivo, 'w')
		entrada = open(directorio+'/test'+str(i)+'/'+archivo,'r')
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

#Genera las tablas a partir del resultado de una simulacion para el modelo con competencia
def crearTablasConCompetencia(directorio, numeroPruebas, archivo):

	for i in range(0, numeroPruebas):
		try:
			os.makedirs(directorio+'/test'+str(i)+'/testTables')
		except OSError as exception:
			if exception.errno != errno.EEXIST:
				raise
		pub1 = open(directorio+'/test'+str(i)+'/testTables/'+'pub1-'+archivo, 'w')
		ener = open(directorio+'/test'+str(i)+'/testTables/'+'energy-'+achivo, 'w')
		aEner = open(directorio+'/test'+str(i)+'/testTables/'+'agentsEnergy-'+archivo, 'w')
		prob1 = open(directorio+'/test'+str(i)+'/testTables/'+'prob1-'+archivo, 'w')
		acumulatedPapers = open(directorio+'/test'+str(i)+'/testTables/'+'acumulated-papers-'+archivo, 'w')
		actualPapers = open(directorio+'/test'+str(i)+'/testTables/'+'actual-papers-'+archivo, 'w')
		pub2 = open(directorio+'/test'+str(i)+'/testTables/'+'pub2-'+archivo, 'w')
		prob2 = open(directorio+'/test'+str(i)+'/testTables/'+'prob2-'+archivo, 'w')
		pub3 = open(directorio+'/test'+str(i)+'/testTables/'+'pub3-'+archivo, 'w')
		prob3 = open(directorio+'/test'+str(i)+'/testTables/'+'prob3-'+archivo, 'w')
		pub4 = open(directorio+'/test'+str(i)+'/testTables/'+'pub4-'+archivo, 'w')
		pub5 = open(directorio+'/test'+str(i)+'/testTables/'+'pub5-'+archivo, 'w')
		pub6 = open(directorio+'/test'+str(i)+'/testTables/'+'pub6-'+archivo, 'w')
		prob4 = open(directorio+'/test'+str(i)+'/testTables/'+'prob4-'+archivo, 'w')
		prob5 = open(directorio+'/test'+str(i)+'/testTables/'+'prob5-'+archivo, 'w')
		prob6 = open(directorio+'/test'+str(i)+'/testTables/'+'prob6-'+archivo, 'w')
		entrada = open(directorio+'/test'+str(i)+'/'+archivo,'r')
		linea=""
		tag=""
		activo=False
		number=0
		for linea in entrada:
			if linea=='"x","y","color","pen down?"\n':
				activo=True;
				continue                   
			if linea=='\n':
				if activo:
					number=number+1;
					active=False;
			if activo:
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
				if number==10:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub4.write(lineaNueva)
				if number==11:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub5.write(lineaNueva)
				if number==12:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub6.write(lineaNueva)
				if number==13:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob4.write(lineaNueva)
				if number==14:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob5.write(lineaNueva)
				if number==15:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob6.write(lineaNueva)
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
		pub4.close()
		pub5.close()
		pub6.close()
		prob4.close()
		prob5.close()
		prob6.close()

#Genera el promedio de los resultados de los distintos tests
def generarPromedioResultado(directorio):
	print "Cuantas pruebas?"
	numberTest = raw_input()
	numberAgentsUniversity1 = ["10000", "1000"]
	numberAgentsUniversity2 = ["10000", "1000"]
	numberAgentsUniversity3 = ["10000", "1000"]
	probabilityIncrease1 = ["0.01", "1.0E-4"]
	probabilityIncrease2 = ["0.01", "1.0E-4", "1.0E-6"]
	probabilityIncrease3 = ["0.01", "1.0E-4", "1.0E-6"]
	initialProbabilityAgents = ["0.01", "1.0E-4", "1.0E-6"]
	initialEnergy = ["100"]
	archivo=""
	for i in numberAgentsUniversity1:
		for j in numberAgentsUniversity2:
			for l in numberAgentsUniversity3:
					for m in probabilityIncrease1:
						for a in probabilityIncrease2:
							for b in probabilityIncrease3:
								for c in initialProbabilityAgents:
									for d in initialEnergy:
										file=i+"-"+j+"-"+l+"-"+m+"-"+a+"-"+b+"-"+c+"-"+d+"-curve.csv"
										obtenerPromedio(directorio, numeroPruebas, archivo)


#Genera el promedio para cada tabla generada
def obtenerPromedio(directorio, numeroPruebas, archivo):
	sumaDatos=[]
	numeroDatos=[]
	try:
		os.makedirs(directory+'/averageResults')
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
	for i in range(0,100):
		sumaDatos.append(0)
		numeroDatos.append(0)
	
	for i in range(0,numeroPruebas):
		pub = open(directorio+'/test'+str(i)+'/'+archivo, 'r')    	    	    
		numeroLinea=0
		for linea in pub:
			linea = linea.replace("\n", '')
			sumaDatos[numeroLinea]=sumaDatos[numeroLinea]+int(linea.split(',')[1])
			numeroDatos[numeroLinea]=numeroDatos[numeroLinea]+1
			numeroLinea=numeroLinea+1
		pub.close()

	pub = open(directorio+'/averageResults/'+archivo, 'w') 

	for i in range(0,100):
		if numeroDatos[i]!=0:
			pub.write(str(i)+','+str(sumaDatos[i]/numeroDatos[i])+'\n')
	pub.close()

#une tablas de resultados
def unirResultados():
	print "What is the directory?"
	directory = raw_input()
	print "How many test?"
	numberTest = int(raw_input())
	file = "test-curve.csv"
	unirTablas(directory,"energy", "publications", file)

#une las tablas seleccionadas
def unirTabla(directory, table1,table2, input):
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

#Genera el promedio de productividad de los agentes
def generarPromedioProductividad():
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
					ordenar(directory,numberTest,file)
	for i in initialEnergy:
		for j in movement:
			for l in probability1:
				for m in probability2:
					file=i+"-"+j+"-"+l+"-"+m+"-turtles.csv"
					generarPromedioProductividadTabla(directory,numberTest,file)

#Ordena las tablas
def ordenar():
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

#Ordena una tabla
def ordenarTabla(directory,numberTest, input):
	for i in range(0,numberTest):
		df = pd.read_csv(directory+'/test'+str(i)+'/'+input, delimiter=",",header=None)
		df.columns = ['id', 'pub']
		df_sort=df.sort_values(by='pub', axis=0,ascending=False)
		df_sort.to_csv(directory+'/test'+str(i)+'/testTables/'+'test'+input, sep=',', index=False, header=None)



#Genera el promedio de productividad para una tabla
def generarPromedioProductividadTabla(directory, numberTest, input):
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

def separarTablas():
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


menu()


