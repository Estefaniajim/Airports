
def function():
	print("Hola")
try:
	airlines = open("airlines.dat", "r", encoding = "UTF-8")
	airports = open("airports.dat", "r", encoding = "UTF-8")
	routes = open("routes.dat", "r", encoding = "UTF-8")
except:
	print("Put the right files")

def ejercicio1(): #Input -- Name of the contry Output -- Airports of the contry
	pais = input("Write the name of the contry")
	i = 0
	print(airports)
	for linea in airports: #Linea is a string
		lista = linea.split(",") #The output if a list of strings

		paisAeropuerto = lista[3]
		if ('"' + pais + '"') == paisAeropuerto:
			i += 1
			nombreAeropuerto = lista[1]
			ciudadAeropuerto = lista[2]
			codigoAeropuerto = lista[4]
			codigo2Aeropuerto = lista[5]
			papa = lista[1] + ", " + lista[2] + ", " + lista[4] + ", " + lista[5]

	try:
		archivo = open("reporteUno.txt", "w")
	except:
		print("error")
	else:
		archivo.write(papa)
		archivo.close()

def ejercicio6():
	#Destinies that the airlines search by the airport
	#The user input airline and the airport, the output is a file with the imformation
	#It also give us the the longest destiny that the airline has.
	#Destinos de una aerolínea desde un determinado aeropuerto.

	inputAerolinea = input("Escribe el nombre de la aerolinea: ")
	inputAeropuerto = input("Escribe el nombre del aeropuerto: ")

	IATAAerolinea = ""
	ICAOAerolinea = ""
	#It search the information of the airline
	for line in airlines:
		lista = line.split(",")
		nombreAerolinea = lista[1]
		if ('"' + inputAerolinea + '"') == nombreAerolinea:
			IATAAerolinea = lista[3] #IATA
			ICAOAerolinea = lista[4] #ICAO
			break

	longitudeAirport = ""
	latitudeAirport = ""
	IATAAirport = ""
	ICAOAirport = ""
	#Find the imformation of the airports to search the destiny
	for line in airports:
		lista = line.split(",")
		nombreAeropuerto = lista[1]
		if ('"' + inputAeropuerto + '"') == nombreAeropuerto:
			IATAAirport = lista[4]
			ICAOAirport = lista[5]
			longitudeAirport = lista[6]
			longitudeAirport =lista[7]
			break

	destinations = [] #Saves the IATA or ICAO codes from the destination airports
	#Find the codes of the airports od the destiny
	for line in routes:
		lista = line.split(",")
		routeAirline = ('"' + lista[0] + '"') #IATA or ICAO
		routeOrigin = ('"' + lista[2] + '"') #IATA or ICAO
		routeDestiny = ('"' + lista[4] +'"') #IATA or ICAO

		if ((routeAirline == IATAAerolinea or routeAirline == ICAOAerolinea) and (routeOrigin == IATAAirport or routeOrigin == ICAOAirport)):
 			#A route from the airline in the searched airport is found
 			destinations.append(routeDestiny)
	print(len(destinations))

	results =
	#Obtain the imformation of each airport destiny and
	#to calculate the resutls and save the imformation on a list
	for line in airports:
		lista = line.split(",")
		tempName = lista[1]
		tempIATA = lista[4]
		tempICAO = lista[5]
		tempLatitude = lista[6]
		tempLongitude = lista[7]
		for i in range(len(destinations)):
			if tempIATA == destinations[i] or tempICAO == destinations[i]:
				distance = float(longitudeAirport)*float(tempLongitude) - float(latitudeAirport)*float(tempLatitude) #Formula de distancia inventada
				results.append([tempName, distance])
				break
	print(len(results))

		#if (tempIATA in destinations) or (tempICAO in destinations):
			#distance = longitudeAirport*tempLongitude - latitudeAirport*tempLatitude #Formula de distancia inventada
			#results.append([tempName, distance])

	#Crear un archivo nuevo e imprimir los resultados como reporte
	try:
		archivo = open("report.txt", "w")
	except:
		print("Error")
	else:
		texto = ""
		for i in range(len(results)):
			texto += "De " + inputAerolinea + " hacia " + results[i][0] + " hay una distancia de " + results[i][1] + "\n"
		archivo.write(texto)
		archivo.close()
