import os
from os import listdir
from os.path import isfile, join
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
	print "2. Separar todas las tablas"
	print "3. Generar el promedio de las tablas de resultado"
	print "4. Unir tablas"
	print "5. Generar el promedio de productividad de los agentes"
	print "6. Limpiar pruebas"
	argumento = input()
	if argumento == 1:
		return separarResultado(directorio)
	elif argumento == 2 :
		return separarTablas(directorio)
	elif argumento == 3:
		return generarPromedioResultado(directorio)
	elif argumento == 4:
		return unirResultados(directorio)
	elif argumento == 5:
		return generarPromedioProductividad(directorio)
	elif argumento == 6:
		return limpiarPruebas(directorio)
	else:
		sys.exit()

def limpiarTestTables(directorio, numeroPruebas):
	for i in range(0, numeroPruebas):
		borrarArchivos(directorio+"/test"+str(i)+"/testTables")

def limpiarPruebas(directorio):
	print "Cuantas pruebas?"
	numeroPruebas = int(raw_input())
	for i in range(0, numeroPruebas):
		borrarArchivos(directorio+"/test"+str(i)+"/")
	limpiarTestTables(directorio, numeroPruebas)



def borrarArchivos(directorio):
	files_dump = [join(directorio, c) for c in listdir(directorio)]
	files_dump = filter(lambda c: isfile(c), files_dump)
	[os.remove(c) for c in files_dump]

#Separa un resultado de la simulacion, en las tablas correspondientes 
def separarResultado(directorio):
	numeroPruebas= 1
	print "Cual es el nombre del archivo?"
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
		pub2 = open(directorio+'/test'+str(i)+'/testTables/'+'pub2-'+archivo, 'w')
		pub3 = open(directorio+'/test'+str(i)+'/testTables/'+'pub3-'+archivo, 'w')
		pub4 = open(directorio+'/test'+str(i)+'/testTables/'+'pub4-'+archivo, 'w')
		pub5 = open(directorio+'/test'+str(i)+'/testTables/'+'pub5-'+archivo, 'w')
		pub6 = open(directorio+'/test'+str(i)+'/testTables/'+'pub6-'+archivo, 'w')
		pub7 = open(directorio+'/test'+str(i)+'/testTables/'+'pub7-'+archivo, 'w')
		pub8 = open(directorio+'/test'+str(i)+'/testTables/'+'pub8-'+archivo, 'w')

		prob1 = open(directorio+'/test'+str(i)+'/testTables/'+'prob1-'+archivo, 'w')
		prob2 = open(directorio+'/test'+str(i)+'/testTables/'+'prob2-'+archivo, 'w')
		prob3 = open(directorio+'/test'+str(i)+'/testTables/'+'prob3-'+archivo, 'w')
		prob4 = open(directorio+'/test'+str(i)+'/testTables/'+'prob4-'+archivo, 'w')
		prob5 = open(directorio+'/test'+str(i)+'/testTables/'+'prob5-'+archivo, 'w')
		prob6 = open(directorio+'/test'+str(i)+'/testTables/'+'prob6-'+archivo, 'w')
		prob7 = open(directorio+'/test'+str(i)+'/testTables/'+'prob7-'+archivo, 'w')
		prob8 = open(directorio+'/test'+str(i)+'/testTables/'+'prob8-'+archivo, 'w')

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
					pub2.write(lineaNueva)
				if number==2:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub3.write(lineaNueva)
				if number==3:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub4.write(lineaNueva)
				if number==4:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub5.write(lineaNueva)
				if number==5:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub6.write(lineaNueva)
				if number==6:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub7.write(lineaNueva)
				if number==7:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub8.write(lineaNueva)
				if number==8:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob1.write(lineaNueva)
				if number==9:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob2.write(lineaNueva)
				if number==10:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob3.write(lineaNueva)
				if number==11:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob4.write(lineaNueva)
				if number==12:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob5.write(lineaNueva)
				if number==13:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob6.write(lineaNueva)
				if number==14:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob7.write(lineaNueva)
				if number==15:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob8.write(lineaNueva)

		entrada.close()
		pub1.close()
		pub2.close()
		pub3.close()
		pub1.close()
		pub2.close()
		pub3.close()
		pub1.close()
		pub2.close()

		prob1.close()
		prob2.close()
		prob3.close()
		prob4.close()
		prob5.close()
		prob6.close()
		prob7.close()
		prob8.close()

#Genera las tablas a partir del resultado de una simulacion para el modelo con competencia
def crearTablasConCompetencia(directorio, numeroPruebas, archivo):
	for i in range(0,numeroPruebas):
		try:
			os.makedirs(directorio+'/test'+str(i)+'/testTables')
		except OSError as exception:
			if exception.errno != errno.EEXIST:
				raise
		pub1 = open(directorio+'/test'+str(i)+'/testTables/'+'pub1-'+archivo, 'w')
		pub2 = open(directorio+'/test'+str(i)+'/testTables/'+'pub2-'+archivo, 'w')
		pub3 = open(directorio+'/test'+str(i)+'/testTables/'+'pub3-'+archivo, 'w')
		pub4 = open(directorio+'/test'+str(i)+'/testTables/'+'pub4-'+archivo, 'w')
		pub5 = open(directorio+'/test'+str(i)+'/testTables/'+'pub5-'+archivo, 'w')
		pub6 = open(directorio+'/test'+str(i)+'/testTables/'+'pub6-'+archivo, 'w')
		pub7 = open(directorio+'/test'+str(i)+'/testTables/'+'pub7-'+archivo, 'w')
		pub8 = open(directorio+'/test'+str(i)+'/testTables/'+'pub8-'+archivo, 'w')

		prob1 = open(directorio+'/test'+str(i)+'/testTables/'+'prob1-'+archivo, 'w')
		prob2 = open(directorio+'/test'+str(i)+'/testTables/'+'prob2-'+archivo, 'w')
		prob3 = open(directorio+'/test'+str(i)+'/testTables/'+'prob3-'+archivo, 'w')
		prob4 = open(directorio+'/test'+str(i)+'/testTables/'+'prob4-'+archivo, 'w')
		prob5 = open(directorio+'/test'+str(i)+'/testTables/'+'prob5-'+archivo, 'w')
		prob6 = open(directorio+'/test'+str(i)+'/testTables/'+'prob6-'+archivo, 'w')
		prob7 = open(directorio+'/test'+str(i)+'/testTables/'+'prob7-'+archivo, 'w')
		prob8 = open(directorio+'/test'+str(i)+'/testTables/'+'prob8-'+archivo, 'w')

		energy = open(directorio+'/test'+str(i)+'/testTables/'+'energy-'+archivo, 'w')
		agentsEnergy = open(directorio+'/test'+str(i)+'/testTables/'+'agentsEnergy-'+archivo, 'w')
		actualPapers = open(directorio+'/test'+str(i)+'/testTables/'+'actualPapers-'+archivo, 'w')

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
					pub2.write(lineaNueva)
				if number==2:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub3.write(lineaNueva)
				if number==3:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub4.write(lineaNueva)
				if number==4:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub5.write(lineaNueva)
				if number==5:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub6.write(lineaNueva)
				if number==6:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub7.write(lineaNueva)
				if number==7:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					pub8.write(lineaNueva)
				if number==8:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob1.write(lineaNueva)
				if number==9:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob2.write(lineaNueva)
				if number==10:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob3.write(lineaNueva)
				if number==11:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob4.write(lineaNueva)
				if number==12:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob5.write(lineaNueva)
				if number==13:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob6.write(lineaNueva)
				if number==14:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob7.write(lineaNueva)
				if number==15:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					prob8.write(lineaNueva)
				if number==16:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					energy.write(lineaNueva)
				if number==17:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					agentsEnergy.write(lineaNueva)
				if number==18:
					lineaNueva=linea.replace(',"0","true"','')
					lineaNueva=lineaNueva.replace('"','')
					actualPapers.write(lineaNueva)

		entrada.close()
		pub1.close()
		pub2.close()
		pub3.close()
		pub1.close()
		pub2.close()
		pub3.close()
		pub1.close()
		pub2.close()

		prob1.close()
		prob2.close()
		prob3.close()
		prob4.close()
		prob5.close()
		prob6.close()
		prob7.close()
		prob8.close()

		energy.close()
		agentsEnergy.close()
		actualPapers.close()

#Genera el promedio de los resultados de los distintos tests
def generarPromedioResultado(directorio):
	print "Cuantas pruebas?"
	numeroPruebas = int(raw_input())
	tiposTabla = ["pub1", "pub2", "pub3", "pub4", "pub5", "pub6", "pub7", "pub8", "prob1", "prob2", "prob3", "prob4", "prob5", "prob6", "prob7", "prob8"]
	initialProbabilityAgents = ["0.01", "0.001", "1.0E-4"]
	archivo=""
	if directorio == "SinCompetencia":
		for a in tiposTabla:
			for c in initialProbabilityAgents:
				archivo= c+"-curve.csv"
				obtenerPromedio(a, directorio, numeroPruebas, archivo)
	else:
		initialEnergy = ["100"]
		sizeIncremented = ["true", "false"]
		for a in tiposTabla:
			for c in initialProbabilityAgents:
				for b in initialEnergy:
					for d in sizeIncremented:
						archivo= c+"-"+b+"-"+d+"-curve.csv"
						obtenerPromedio(a, directorio, numeroPruebas, archivo)


#Genera el promedio para cada tabla generada
def obtenerPromedio(tipoTabla, directorio, numeroPruebas, archivo):
	sumaDatos=[]
	numeroDatos=[]
	archivo = tipoTabla+"-"+archivo
	try:
		os.makedirs(directorio+'/averageResults')
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
	for i in range(0,500):
		sumaDatos.append(0)
		numeroDatos.append(0)
	
	for i in range(0,numeroPruebas):
		info = open(directorio+'/test'+str(i)+'/'+"testTables/"+archivo, 'r')    	    	    
		numeroLinea=0
		for linea in info:
			linea = linea.replace("\n", '')
			if tipoTabla == "pub1" or tipoTabla == "pub2" or tipoTabla == "pub3" or tipoTabla == "pub4" or tipoTabla == "pub5" or tipoTabla == "pub6" or tipoTabla == "pub7" or tipoTabla == "pub8":
				sumaDatos[numeroLinea]=sumaDatos[numeroLinea]+int(linea.split(',')[1])
			else:
				sumaDatos[numeroLinea]=sumaDatos[numeroLinea]+float(linea.split(',')[1])
			numeroDatos[numeroLinea]=numeroDatos[numeroLinea]+1
			numeroLinea=numeroLinea+1
		info.close()

	info = open(directorio+'/averageResults/'+archivo, 'w') 

	for i in range(500):
		if numeroDatos[i]!=0:
			info.write(str(i)+','+str(sumaDatos[i]/numeroDatos[i])+'\n')
	info.close()



#une tablas de resultados
def unirResultados(directorio):
	print "Cuantas pruebas?"
	numeroPruebas = int(raw_input())
	initialProbabilityAgents = ["0.01", "0.001", "1.0E-4"]
	archivo=""
	if directorio == "SinCompetencia":
		for c in initialProbabilityAgents:
			archivo= c+"-curve.csv"
			unirTablas(directorio,"prob", "pub", numeroPruebas, archivo)
	else:
		initialEnergy = ["100"]
		sizeIncremented = ["true", "false"]
		for c in initialProbabilityAgents:
			for b in initialEnergy:
				for a in sizeIncremented:
					archivo= c+"-"+b+"-"+a+"-curve.csv"
					unirTablas(directorio,"prob", "pub",numeroPruebas, archivo)
	

#une las tablas seleccionadas
def unirTablas(directorio, table1,table2,numeroPruebas, archivo):
	listOfNumbers=[]
	for i in range(0,3002):
		listOfNumbers.append(0)
	try:
		os.makedirs(directorio+'/averageResults/')
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
	for i in range(1, 9):
		tab1 = open(directorio+'/averageResults/'+table1+str(i)+"-"+archivo, 'r')
		tab2 = open(directorio+'/averageResults/'+table2+str(i)+"-"+archivo, 'r')
		entrada = open(directorio+'/averageResults/'+table1+'-'+table2+"-"+str(i)+"-"+archivo,'w')
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
def generarPromedioProductividad(directorio):
	print "Cuantas pruebas?"
	numeroPruebas = int(raw_input())
	if directorio == "SinCompetencia":
		initialProbabilityAgents = ["0.01", "0.001", "1.0E-4"]
		archivo=""
		for c in initialProbabilityAgents:
			archivo= c+"-turtles.csv"
			ordenarTabla(directorio, numeroPruebas, archivo)
		for c in initialProbabilityAgents:
			archivo= c+"-turtles.csv"
			generarPromedioProductividadTabla(directorio, numeroPruebas, archivo)
	else:
		initialProbabilityAgents = ["0.01", "0.001", "1.0E-4"]
		initialEnergy = ["100"]
		sizeIncremented = ["true", "false"]
		archivo=""
		for c in initialProbabilityAgents:
			for b in initialEnergy:
				for a in sizeIncremented:
					archivo= c+"-"+b+"-"+a+"-turtles.csv"
					ordenarTabla(directorio, numeroPruebas, archivo)	
		for c in initialProbabilityAgents:
			for b in initialEnergy:
				for a in sizeIncremented:
					archivo= c+"-"+b+"-"+a+"-turtles.csv"
					generarPromedioProductividadTabla(directorio, numeroPruebas, archivo)



#Ordena una tabla
def ordenarTabla(directorio, numeroPruebas, archivo):
	for i in range(0, numeroPruebas):
		df = pd.read_csv(directorio+'/test'+str(i)+'/'+archivo, delimiter=",",header=None)
		df.columns = ['id', 'pub', 'uni']
		df_sort=df.sort_values(by='pub', axis=0,ascending=False)
		df_sort.to_csv(directorio+'/test'+str(i)+'/testTables/'+'order-'+archivo, sep=',', index=False, header=None)

#Genera el promedio de productividad para una tabla
def generarPromedioProductividadTabla(directorio, numeroPruebas, archivo):
	sumaDatos = []
	numeroDatos = []
	universidades = []
	try:
		os.makedirs(directorio+'/averageResults')
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
	for i in range(0,4401):
		sumaDatos.append(0)
		numeroDatos.append(0)
		universidades.append(0)
	
	for i in range(0,numeroPruebas):
		info = open(directorio+'/test'+str(i)+'/'+"testTables/"+"order-"+archivo, 'r')    	    	    
		numeroLinea=0
		for linea in info:
			linea = linea.replace("\n", '')
			sumaDatos[numeroLinea] = sumaDatos[numeroLinea]+int(linea.split(',')[1])
			numeroDatos[numeroLinea] = numeroDatos[numeroLinea]+1
			universidades[numeroLinea] = linea.split(',')[2]
			numeroLinea=numeroLinea+1
		info.close()

	info = open(directorio+'/averageResults/'+archivo, 'w') 

	for i in range(0,4401):
		if numeroDatos[i]!=0:
			info.write(universidades[i]+','+str(sumaDatos[i]/numeroDatos[i])+'\n')
	info.close()

def separarTablas(directorio):
	print "Cuantas pruebas?"
	numeroPruebas = int(raw_input())
	initialProbabilityAgents = ["0.01", "0.001", "1.0E-4"]
	archivo=""
	if directorio == "SinCompetencia":
		for c in initialProbabilityAgents:
			archivo= c+"-curve.csv"
			crearTablasSinCompetencia(directorio, numeroPruebas, archivo)
	else:
		initialEnergy = ["100"]
		sizeIncremented = ["true", "false"]
		for c in initialProbabilityAgents:
			for b in initialEnergy:
				for a in sizeIncremented:
					archivo= c+"-"+b+"-"+a+"-curve.csv"
					crearTablasConCompetencia(directorio, numeroPruebas, archivo)
			


menu()


