def armar_dic(path) :
	lista = []
	dic = {}
	archivo = open(path)
	for linea in archivo.readlines() :
		linea = linea[:-1]
		lista = linea.split("|")
		dic.setdefault(lista[0],int(lista[-1]))
	archivo.close()
	return dic

def actualizar_archivo(path, dic) :
	print dic
	archivo = open(path,"r+")
	archivo.readlines()
	tam_linea = archivo.tell()
	archivo.seek(0,0)
	for linea in archivo.readlines() :
		linea = linea[:-1]
		lista = linea.split("|")
		print lista
		aumento = dic.get(lista[1])
		print aumento
		if aumento == None :
			continue
		aumento = float(aumento) / (100) + 1
		print aumento
		para_atras = tam_linea * -1
		print para_atras
		archivo.seek(para_atras,1)
		archivo.write(lista[0]+"|"+lista[1]+"|")
		print lista[-1]
		sueldo_actual = float(lista[-1]) * aumento
		print sueldo_actual
		archivo.write(str(sueldo_actual)+"\n")
		archivo.seek(0,1)

path_lista = "C:/Users/folivera/Documents/Python/lista_empleados.txt"
path_aumentos = "C:/Users/folivera/Documents/Python/empleados_aumento.txt"
dic_aumentos = armar_dic(path_aumentos)
actualizar_archivo(path_lista, dic_aumentos)