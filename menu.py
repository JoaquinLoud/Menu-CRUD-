def opciones():
    diccionario = {}
    salir = False
    while (salir == False):
     tamañao = len(diccionario)
     print("Bienvenido Al Menu\n\n")
     print("1............AGREGAR")
     print("2............MOSTRAR")
     print("3............EDITAR")
     print("4............ELIMINAR")
     print("5............SALIR")
    opcion = int(input("Digite una opcion: "))
    
    if (opcion ==1):
        tamañao = len(diccionario)
        try:
             funcion = input("Digite el nombre de la funcion: ")
             descripcionFun = input("Digite la descripcion de la Funcion: ")
             diccionario[tamañao + 1] = (descripcionFun, funcion)
        except:
             print('Error dato invalido')
             print(diccionario)
    
        
    if (opcion == 4):
            if(tamañao > 0):
                print("Bienvenido Al Listado de funciones\n\n")
                for x in diccionario:
                    print(f"{x}. {diccionario[x][0]}")
                salida = False
                while (salida == False):
                    try:
                        op = int(input("Digite una opcion para eliminar: "))
                        salida = True
                    except:
                        print('Error dato Invalido')
                new = {}
                for clave in diccionario:
                    if (op != clave): 
                        new[clave] = (diccionario[clave][0], diccionario[clave][1])
                diccionario = new; 
            else: 
                print('\n\n" No se han agregado Funciones...')
                if (opcion == 5):
                    salir = True



if __name__ == '_main_':

    opciones()
