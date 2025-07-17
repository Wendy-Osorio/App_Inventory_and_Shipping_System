#Se agrega la libreria tabulate para mostrar los datos en una tabla
from tabulate import tabulate

# Se declaran las listas que almacenaran los articulos, cantidad y peso
articulos = [[], [], []]

pesoProd = []

cantProd = []

# Se declara la variable tamaño
tamaño = 1

# Se declara la funcion menuPrincipal que es el menu principal del programa
def menuPrincipal():

    # Se muestra el menu principal
    print('Welcome to the product inventory and shipping system.\nMenu: \n1. Add items \n2. Delete items \n3. View item \n4. Quote shipping \n5. Edit product \n6. Exit')

    # Se solicita al usuario que ingrese una opcion
    resp = input('What operation do you want to perform?: ')

    # Se valida la entrada del usuario
    try:

        # Si el usuario ingresa una cadena, se convierte a entero
        resp = int(resp)


        #Agregar articulos
        if resp == 1:

            addArticles()
        
        else:
            
            #Eliminar articulos
            if resp == 2:

                deleteArticles()

            else:
                
                #Ver articulos
                if resp == 3:

                    verArticulos()

                else:
                    
                    #Cotizar envios
                    if resp == 4:
            
                        envio()

                    else:

                        #Salir del programa
                        if resp == 5:

                            editProduct()
                        
                        else:

                            if resp == 6:

                                exit()
                            
                            else:

                                # Si el usuario ingresa un valor que no es una opcion valida, se imprime un mensaje de error
                                print('\nERROR!: THE DATA ENTERED IS INVALID... TRY AGAIN\n')

                                # Se vuelve a mostrar el menu principal
                                menuPrincipal()

    # Si el usuario ingresa un valor que no es un entero, se captura la excepcion
    except ValueError:

        #print('ERROR YOU ENTERED AN INVALID OPTION...TRY AGAIN.\n')

        # Se vuelve a mostrar el menu principal
        menuPrincipal()

#Se define la funcion addArticles que agrega articulos a la lista de articulos
def addArticles():

    #Mensajes para el usuario
    print('\nNOTE: To exit press the "/ + Enter" key\n')
    print("\n>>ENTER PRODUCT DATA<<\n")

    # Se muestran los mensajes indicando al usuario que se van a ingresar los datos del producto
    nombre = input("Product name: ")

    # Si el usuario no ingresa un nombre, se imprime un mensaje de error
    if nombre == '':

        print('\nERROR!: THE DATA ENTERED IS INVALID... TRY AGAIN\n')

        # Se vuelve a llamar a la funcion addArticles para que el usuario ingrese los datos nuevamente
        addArticles()

    else:

        #Si el usuario ingresa '/', se regresa al menu principal
        if nombre == '/':

            menuPrincipal()
            
        cantidad = input("Units: ")

        if cantidad == '/':

            menuPrincipal()

        peso = input("Weight(Kg): ")

        if peso == '/':

            menuPrincipal()

        # Se valida la entrada del usuario
        try:

            # Se convierte la cantidad y el peso a enteros
            cantidad = int(cantidad)

            # Se convierte el peso a float
            peso = float(peso)

            #Se agrega la cantidad y el peso a las listas correspondientes
            cantProd.append(cantidad)

            pesoProd.append(peso)

            #Se formatean los datos y se les agregan caracteres descriptivos
            nombre = 'Name: ' + nombre.capitalize()

            peso = 'Weight: ' + str(peso) + ' Kg' 

            cantidad = 'Units: ' + str(cantidad)

            #Se agregan los datos a la lista de listas de los articulos
            articulos[0].append(nombre)

            # La segunda lista es para cantidad
            articulos[1].append(cantidad)

            #peso
            articulos[2].append(peso)

            # Se imprime un mensaje indicando que el articulo ha sido agregado
            print("\nThe article has been successfully added...")

            # Se llama a la funcion respAdd para preguntar si se desea agregar otro articulo
            respAdd()

        # Si el usuario ingresa un valor que no es un entero o float, se captura la excepcion
        except ValueError:
                
                #Se valida la entrada del usuario nuevamente 
                try: 

                    #Se valida la entrada del usuario si es un valor entero
                    cantidad = int(cantidad)

                    #Se valida la entrada del usuario si es un valor entero
                    peso = int(peso)

                    #Se agrega la cantidad y el peso a las listas correspondientes
                    cantProd.append(cantidad)

                    pesoProd.append(peso)

                    #Se formatean los datos y se les agregan caracteres descriptivos
                    nombre = 'Name: ' + nombre.capitalize()

                    peso = 'Weight: ' + str(peso) + ' Kg' 

                    cantidad = 'Units: ' + str(cantidad)

                    # La primera lista es para los nombres
                    articulos[0].append(nombre)

                    # La segunda lista es para cantidad
                    articulos[1].append(cantidad)

                    #peso
                    articulos[2].append(peso)

                    # Se imprime un mensaje indicando que el articulo ha sido agregado
                    print("\nThe article has been successfully added...")

                    # Se llama a la funcion respAdd para preguntar si se desea agregar otro articulo
                    respAdd()
                
                # Si el usuario ingresa un valor que no es un entero o float, se captura la excepcion
                except ValueError:

                    # Se imprime un mensaje indicando que el dato ingresado es invalido
                    print('\nERROR!: THE DATA ENTERED IS INVALID... TRY AGAIN\n')

                    # Se vuelve a llamar a la funcion addArticles para que el usuario ingrese los datos nuevamente
                    addArticles()

#Se define la funcion respAdd que pregunta si se desea agregar otro articulo
def respAdd():

        # Se pregunta al usuario si desea agregar otro articulo
        repuesta = input('\nWant to add another item? Y/N: ')

        # Se valida la entrada del usuario
        if repuesta.lower() == 'y':

            # Si el usuario desea agregar otro articulo, se llama a la funcion addArticles
            addArticles()

        # Si el usuario no desea agregar otro articulo, se regresa al menu principal    
        if repuesta.lower() == 'n':

            menuPrincipal()

        # Si el usuario ingresa un valor que no es 'y' o 'n', se imprime un mensaje de error
        else:

            print('\nERROR!: THE DATA ENTERED IS INVALID...\n')

            menuPrincipal()

#Se define la funcion verArticulos que muestra los articulos registrados
def verArticulos():

    # Se imprime la lista de articulos registrados mediante la libreria tabulate
    print('\nTABLE OF REGISTERED ARTICLES\n')

    table = tabulate(
        articulos,
        rowalign=('Nombre, cantidad, peso'),
        tablefmt="grid"
    )

    print(table)

    # Se imprime un mensaje indicando que se puede regresar al menu principal
    resp_ver()

#Se define la funcion resp_ver que pregunta si se desea regresar al menu principal
def resp_ver():

    # Se pregunta al usuario si desea regresar al menu principal
    print('\nTo return to the main menu press the "X" key\n')

    # Se solicita al usuario que ingrese una respuesta
    repuesta = input('\n>>: ')

    # Se valida la entrada del usuario
    if repuesta.lower() == 'x':

            menuPrincipal()

    # Si el usuario ingresa un valor que no es 'x', se imprime un mensaje de error
    else:

        print('\n¡ERROR!: LOS DATOS INGRESADOS NO SON VALIDOS...\n')

        verArticulos()

#Se define la funcion deleteArticles que elimina un articulo de la lista de articulos
def deleteArticles():
    
    # Se imprime un mensaje indicando que se va a eliminar un articulo
    print('\nNOTE: To exit press the "/ + Enter" key\n')
    product = input('\nEnter the name of the item you want to delete: ')

    # Si el usuario ingresa '/', se regresa al menu principal
    if product == '/':

        menuPrincipal()

    # Se formatea el nombre del producto para que comience con mayuscula
    product = 'Name: ' + product.capitalize() 

    # Se asigna el nombre del producto a la variable product
    product = product

    # Se intenta encontrar el producto en la lista de articulos
    try:

        # Se obtiene la posicion del producto en la lista de articulos
        posicion = articulos[0].index(product)

        # Se elimina el producto de las listas correspondientes
        cantProd.pop(posicion)

        pesoProd.pop(posicion)

        articulos[0].pop(posicion)

        articulos[1].pop(posicion)

        articulos[2].pop(posicion)

        # Se imprime un mensaje indicando que el articulo ha sido eliminado
        print('\nThe article has been successfully deleted...')

        # Se llama a la funcion resp_delete para preguntar si se desea eliminar otro articulo
        resp_delete()

    # Si el producto no se encuentra en la lista de articulos, se captura la excepcion
    except ValueError:

        print('\nERROR!: THE DATA ENTERED IS INVALID... TRY AGAIN\n')

        deleteArticles()

#Se define la funcion resp_delete que pregunta si se desea eliminar otro articulo
def resp_delete():

    # Se pregunta al usuario si desea eliminar otro articulo
    repuesta = input('\nDo you want to delete another item? Y/N: ')

    # Se valida la entrada del usuario
    if repuesta.lower() == 'y':

        deleteArticles()

    if repuesta.lower() == 'n':

        menuPrincipal()

    # Si el usuario ingresa un valor que no es 'y' o 'n', se imprime un mensaje de error
    else:

        print('\nERROR!: THE DATA ENTERED IS INVALID...\n')

        menuPrincipal()

#Se define la funcion envio que cotiza el envio de un articulo
def envio():

    # Se imprime un mensaje indicando que se va a cotizar el envio de un articulo
    print('\nNOTE: To exit press the "/ + Enter" key\n')
    prod_Buscar = input('\nEnter the product name: ')

    # Si el usuario ingresa '/', se regresa al menu principal
    if prod_Buscar == '/':

        menuPrincipal()

    # Se formatea el nombre del producto para que comience con mayuscula
    prod_Buscar = 'Name: ' + prod_Buscar.capitalize()

    prod_Buscar = prod_Buscar

    # Se intenta encontrar el producto en la lista de articulos
    try:

        # Se obtiene la ubicacion del producto en la lista de articulos
        ubicacion = articulos[0].index(prod_Buscar)

        cantProds = cantProd[ubicacion]

        pesoPq = pesoProd[ubicacion]

        # Se indica el costo de envio por producto
        costoEnvio = 35.99

        # Se calcula el costo total de envio mediante el peso, la cantidad de productos y el costo de envio por producto
        costo_Envio = ((pesoPq * cantProds) + costoEnvio) 

        # Se imprime el costo total de envio
        print('\nThe cost of shipping your package is ${} MXN\nShipping cost per package: $35.99 MXN\n'.format(costo_Envio))

        # Se llama a la funcion respEnvio para preguntar si se desea cotizar otro envio
        respEnvio()

    # Si el producto no se encuentra en la lista de articulos, se captura la excepcion
    except ValueError:

        print('\nERROR!: THE DATA ENTERED IS INVALID... TRY AGAIN\n')

        envio()

#Se define la funcion respEnvio que pregunta si se desea cotizar otro envio
def respEnvio():

    # Se pregunta al usuario si desea cotizar otro envio
    repuesta = input('\nWould you like to check the shipping cost for another product? Y/N: ')

    # Se valida la entrada del usuario
    if repuesta.lower() == 'y':

        envio()

    if repuesta.lower() == 'n':

        menuPrincipal()

    # Si el usuario ingresa un valor que no es 'y' o 'n', se imprime un mensaje de error
    else:

        print('\nERROR!: THE DATA ENTERED IS INVALID...\n')

        menuPrincipal()

# Se define la funcion editProduct que permite editar un producto
def editProduct():

    # Se imprime un mensaje indicando que se va a editar un producto
    print('\nNOTE: To exit press the "/ + Enter" key\n')
    product = input('\nEnter the name of the item you want to edit: ')

    # Si el usuario ingresa '/', se regresa al menu principal
    if product == '/':

        menuPrincipal()

    # Se formatea el nombre del producto para que comience con mayuscula
    product = 'Name: ' + product.capitalize() 

    product = product

    # Se intenta encontrar el producto en la lista de articulos
    try:

        # Se obtiene la posicion del producto en la lista de articulos
        posicion = articulos[0].index(product)

        # Se solicita al usuario que ingrese los nuevos datos del producto
        new_name = input('Enter the new name of the product: ')
        new_quantity = input('Enter the new quantity of the product: ')
        new_weight = input('Enter the new weight of the product: ')

        # Se valida la entrada del usuario
        try:

            # Se convierte la cantidad y el peso a enteros y float respectivamente
            new_quantity = int(new_quantity)
            new_weight = float(new_weight)

            # Se actualizan los datos del producto en las listas correspondientes
            articulos[0][posicion] = 'Name: ' + new_name.capitalize()
            articulos[1][posicion] = 'Units: ' + str(new_quantity)
            articulos[2][posicion] = 'Weight: ' + str(new_weight) + ' Kg'

            # Se actualizan las listas de cantidad y peso
            cantProd[posicion] = new_quantity
            pesoProd[posicion] = new_weight

            print('\nThe product has been successfully edited...')

            resp_edit()

        except ValueError:
            print('\nERROR!: THE DATA ENTERED IS INVALID... TRY AGAIN\n')
            editProduct()

    except ValueError:
        print('\nERROR!: THE DATA ENTERED IS INVALID... TRY AGAIN\n')
        editProduct()

def resp_edit():

    # Se pregunta al usuario si desea editar otro producto
    repuesta = input('\nDo you want to edit another product? Y/N: ')

    # Se valida la entrada del usuario
    if repuesta.lower() == 'y':

        editProduct()

    if repuesta.lower() == 'n':

        menuPrincipal()

    # Si el usuario ingresa un valor que no es 'y' o 'n', se imprime un mensaje de error
    else:

        print('\nERROR!: THE DATA ENTERED IS INVALID...\n')

        menuPrincipal()

# Se llama a la funcion menuPrincipal para iniciar el programa
menuPrincipal()

