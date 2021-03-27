import csv

switch= True
resp= 1
tabla= list()

while switch:
    print("{1}.AGREGAR CLIENTE")
    print("{2}.BUSCAR CLIENTE")
    print("{3}.CONSULTAR TODOS LOS CLIENTES")
    print("{4}.SALIR")
    opcion= int(input("SELECCIONE UNA OPCION"))
    if opcion==1:
        while resp==1:
            nombre= input("Nombre ")
            tel= int(input("Telefono "))
            calle= input("Calle ")
            numext= input("Numero Ext.")
            coln= input("Colonia ")
            tabla.append([nombre, tel, calle, numext, coln])
            
            with open('clientes4.csv', 'a+', newline="") as arch:
                add= csv.writer(arch)
                
                add.writerows(tabla)
                
                resp= int(input("¿DESEA AGREGAR OTRO CLIENTE? (1=SI)\(2=NO)"))
    
    elif opcion==2:
        buscar=int(input("INGRESE EL TELEFONO DEL CLIENTE"))
        for registro in tabla:
            if registro[1]==buscar:
                print(registro)
                break
        else:
            print("NO EXISTE")
    
    elif opcion==3:
        for regis in tabla:
            print(regis)
    
    elif opcion==4:
        switch= False