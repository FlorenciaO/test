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

def actualizar_archivo(path, dic) :
	archivo = open(path,"r+")
	pos = archivo.tell()
	for linea in archivo.readlines() :
		procesar_linea(archivo, linea, dic)

def procesar_linea(archivo, linea, dic):
	tam_linea = archivo.tell() - pos
	linea = linea[:-1]
	lista = linea.split("|") 				# Me armo una pequenia lista en cada iteracion por cada empleado con sus datos como elementos de la lista
	aumento = dic.get(lista[1]) 			# Si el dni de la lista se encuentra en el dic me devuelve el porcentaje de aumento, sino me devuelve un objeto None
	if aumento == None :
		archivo.write(lista[0]+"|"+lista[1]+"|"+lista[-1]+"\n")	# Si no esta el dni en el dic, escribo con la misma informacion obtenida
	else :
		aumento = float(aumento) / (100) + 1 	# Convierto en un flotante el porcentaje
		archivo.seek(tam_linea * -1,1)
		archivo.write(lista[0]+"|"+lista[1]+"|")
		print lista[-1]
		sueldo_actual = float(lista[-1]) * aumento
		archivo.write(str(sueldo_actual)+"\n")
	pos = archivo.tell()

path_lista = "lista_empleados.txt"
path_aumentos = "empleados_aumento.txt"
dic_aumentos = armar_dic(path_aumentos)
print dic_aumentos
actualizar_archivo(path_lista, dic_aumentos)
