def armar_dic(path) :
	lista = []
	dic = {}
	archivo = open(path)
	for linea in archivo.readlines() :
		linea = linea[:-1]
		lista = linea.split("|")
		dic.setdefault(lista[0],int(lista[-1])) # Me armo un dic en base a cada registro del archivo de aumentos con el dni como key
	archivo.close()
	return dic

def actualizar_archivo(path, dic_aumentos) :
	lista_emp = crear_lista(path)
	actualizar_lista(dic_aumentos, lista_emp)
	sobreescribir_archivo(path, lista_emp)

def crear_lista(path) :
	archivo = open(path,"r")
	lista = []
	for linea in archivo.readlines() :
		procesar_linea(archivo, linea, lista)
	archivo.close()
	return lista

def procesar_linea(archivo, linea, lista) :
	linea = linea[:-1]
	sublista = linea.split("|")
	lista.append(sublista)

def actualizar_lista(dic_aum, lista) :
	for x in range(len(lista)) :
		aumento = dic_aum.get(lista[x][1])
		if aumento != None :
			sueldo_actual = float(lista[x][-1]) * ( float(aumento) / 100 + 1 )
			print sueldo_actual
			lista[x][-1] = str(sueldo_actual)

def sobreescribir_archivo(path, lista) :
	archivo = open(path, "w")
	for elementos in lista :
		linea = elementos[0]+"|"+elementos[1]+"|"+elementos[-1]+"\n"
		archivo.write(linea)
	archivo.close()


path_lista = "lista_empleados.txt"
path_aumentos = "empleados_aumento.txt"
dic_aumentos = armar_dic(path_aumentos)
actualizar_archivo(path_lista, dic_aumentos)
