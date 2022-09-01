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
    
    if (opcion == 1):
            tamañao = len(diccionario)
            try:
                funcion = input("Digite el nombre de la funcion: ")
                descripcionFun = input("Digite la descripcion de la funcion: ")
                diccionario[tamañao + 1] = (descripcionFun, funcion)
            except:
                print('Error dato invalido')
            print(diccionario)
  