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
<<<<<<< HEAD
	pos = archivo.tell()
	for linea in archivo.readlines() :
		tam_linea = archivo.tell() - pos
		linea = linea[:-1]
		lista = linea.split("|") 					# Me armo una pequenia lista en cada iteracion por cada empleado con sus datos como elementos de la lista
		print lista
		aumento = dic.get(lista[1]) 				# Si el dni de la lista se encuentra en el dic me devuelve el porcentaje de aumento, sino me devuelve un objeto None
		if aumento == None :
			archivo.write(lista[0]+"|"+lista[1]+"|"+lista[-1]+"\n")	# Si no esta el dni en el dic, sigo recorriendo el archivo salteandome las siguientes sentencias
		else :
			aumento = float(aumento) / (100) + 1 		# Convierto en un flotante el porcentaje
			archivo.seek(tam_linea * -1,1)
			archivo.write(lista[0]+"|"+lista[1]+"|") 	# Vuelvo a escribir el nombre, apellido y dni con los separadores 
			sueldo_actual = float(lista[-1]) * aumento
			archivo.write(str(sueldo_actual)+"\n")		# Actualizo sueldo
		pos = archivo.tell()
		
=======
	archivo.readlines()
	tam_linea = archivo.tell()					# Guardo el tamanio de un registro para luego poder retroceder en el archivo esa cantidad de bytes
	archivo.seek(0,0)
	for linea in archivo.readlines() :
		procesar_linea(archivo, tam_linea, linea, dic)

def procesar_linea(archivo, tam_linea, linea, dic):
	linea = linea[:-1]
	lista = linea.split("|") 				# Me armo una pequenia lista en cada iteracion por cada empleado con sus datos como elementos de la lista
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
>>>>>>> 95f83b0fd041c3a71d114ee17d28d18ac1cd3b32

path_lista = "lista_empleados.txt"
path_aumentos = "empleados_aumento.txt"
dic_aumentos = armar_dic(path_aumentos)
print dic_aumentos
actualizar_archivo(path_lista, dic_aumentos)