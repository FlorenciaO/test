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
	print dic
	archivo = open(path,"r+")
	archivo.readlines()
	tam_linea = archivo.tell()					# Guardo el tamaño de un registro para luego poder retroceder en el archivo esa cantidad de bytes
	archivo.seek(0,0)
	for linea in archivo.readlines() :
		procesar_linea(archivo, tam_linea, linea, dic)

def procesar_linea(archivo, tam_linea, linea, dic):
	linea = linea[:-1]
	lista = linea.split("|") 				# Me armo una pequeña lista en cada iteracion por cada empleado con sus datos como elementos de la lista
	aumento = dic.get(lista[1]) 			# Si el dni de la lista se encuentra en el dic me devuelve el porcentaje de aumento, sino me devuelve un objeto None
	print aumento
	if aumento == None :
		return  
	print lista							# Si no esta el dni en el dic, sigo recorriendo el archivo salteandome las siguientes sentencias
	"""aumento = float(aumento) / (100) + 1 	# Convierto en un flotante el porcentaje
	para_atras = tam_linea * -1
	print para_atras
	archivo.seek(para_atras,1)
	archivo.write(lista[0]+"|"+lista[1]+"|")
	print lista[-1]
	sueldo_actual = float(lista[-1]) * aumento
	print sueldo_actual
	archivo.write(str(sueldo_actual)+"\n")
	archivo.seek(0,1)"""

path_lista = "lista_empleados.txt"
path_aumentos = "empleados_aumento.txt"
dic_aumentos = armar_dic(path_aumentos)
print dic_aumentos
actualizar_archivo(path_lista, dic_aumentos)