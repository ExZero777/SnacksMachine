

class snacks:
    nombre_snacks=""
    cantidad_snacks=""
    precio_snacks=""
    
class ingreso:
    nombre_ingreso=""
    apellido_ingreso=""
    dni_ingreso=""
    codigo_ingreso=""
    permiso_ingreso=""
    
class gestion:
    nombre_gestion=""
    precio_gestion=""
    cantidad_gestion=""
    
class totales:
    codigo_totales=""
    fecha_totales=""
    horario_totales=""
    gestion_totales=""
    subtotal_totales=""
    total_totales=""
    


def gestion(ge,o):
    if(o==0):
       if(ge==1):
          f = open("snacks.txt","a")
          snacks.nombre_snacks = input(str("Ingrese El Nuevo Snack: "))
          snacks.precio_snacks = input(str("Ingrese El Precio Del Snack: "))
          snacks.cantidad_snacks= input(str("Ingrese La Cantidad Del Snack: "))
          f.write(snacks.nombre_snacks+","+snacks.precio_snacks+","+snacks.cantidad_snacks+"\n")
          print("Ingreso Exitoso")
          f.close()
        
       if(ge==2):
          f = open("snacks.txt","r")
          i = 0   
          for aline in f:
             values = aline.split()
             print(" %4d: %s" %(i, values))
             i+=1
          f.close()
        
          f = open("snacks.txt","r")
          lines = f.readlines()
          f.close()
        
          lineas= input("Ingrese El Número De Snack A Borrar!!: ")
          del lines[int(lineas)]
          f = open("snacks.txt","w")
          for line in lines:
              f.write(line)
              print("Borrado Exitoso ")
          else:
             print("Error,Ingrese Nuevamente El Indice") 
          f.close()
       
               
       if(ge==3):
          print("Lista De Snacks") 
          f = open("snacks.txt")
          i = 1
          for linea in f:
              linea = linea.rstrip("\\n")
              print(" %4d: %s" %(i, linea))
              i+=1
          f.close()
                  
        
       if(ge==4):
          f = open("ingreso.txt","a")
          ingreso.nombre_ingreso = input(str("Ingrese El Nombre Del Usuario: "))
          ingreso.apellido_ingreso = input(str("Ingrese El Apellido Del Usuario: "))
          ingreso.dni_ingreso = input(str("Ingrese El Dni Del Usuario: "))
          ingreso.codigo_ingreso= input(str("Ingrese El Codigo Del Usuario: "))
          ingreso.permiso_ingreso=input(str("Ingrese El Permiso Del Usuario: "))
          f.write(ingreso.nombre_ingreso+","+ingreso.apellido_ingreso+","+ingreso.dni_ingreso+","+ingreso.codigo_ingreso+","+ingreso.permiso_ingreso+"\n")
          print("Ingreso Exitoso")
          f.close()
        
       if(ge==5):
           f = open("ingreso.txt","r")
           i = 0   
           for aline in f:
              values = aline.split()
              print(" %4d: %s" %(i, values))
              i+=1
           f.close()
       
           f = open("ingreso.txt","r")
           lines = f.readlines()
           f.close()
       
           lineas= input("Ingrese El Nombre Del Usuario A Borrar!!: ")
           del lines[int(lineas)]
           f = open("ingreso.txt","w")
           for line in lines:
              f.write(line)
              print("Borrado Exitoso ")
           else:
              print("Error,Ingrese Nuevamente El Indice") 
           f.close()

       if(ge==6):
           print("Lista De Usuarios") 
           f = open("ingreso.txt")
           i = 1
           for linea in f:
               linea = linea.rstrip("\\n")
               print(" %4d: %s" %(i, linea))
               i+=1
           f.close()
       if(ge==7):
            exit
        

    elif(o>0):
        if(ge==1):
            print("-----------Snacks------------")
            print("---Snack--Precio--Cantidad---")
            f = open("snacks.txt")
            i = 1
            for linea in f:
               linea = linea.rstrip("\\n")
               print(" %4d: %s" %(i, linea))
               i+=1
            f.close()
            print("-----------------------------") 
        cg=input(str("Ingrese La Cantidad De Snacks A Llevar: "))
        f=open("snacks.txt","r")
        for cant in cg:
            
        
            

def maquina(op):
    ges=0
    if(op==0):
        print("----------Menu----------")
        print("1-Ingreso De Snacks")
        print("2-Egreso De Snacks")
        print("3-Ver Snacks")
        print("4-Ingreso De Codigos")
        print("5-Eliminar De Codigos")
        print("6-Ver Codigos")
        print("7-Salir")
        print("------------------------")
        ges=int(input("Favor De Ingresar Una Opcion Para Operar: "))
        gestion(ges,op)
    elif(op>0):
        print("----------Menu----------")
        print("1-Snacks Para Llevar")
        print("2-")
        print("3-Salir")
        print("------------------------")
        ges=int(input("Favor De Ingresar Una Opcion Para Operar: "))
        gestion(ges,op)

def ingreso():
    opcion=1
    print("Bienvenido A La Maquina De Snacks!!!")
    while ((opcion > 0)  and (opcion!= 0)):
        print("Favor Ingrese Su Codigo Para Empezar")
        opcion = int(input("El Codigo Es Númerico Y Se Lo Tiene Que Proporcionar RR.HH: "))
        maquina(opcion)
    else:
        print("El Codigo Ingresado Es Incorrecto, Favor De Ingresarlo Nuevamente O Comunicarse Con RR.HH")
        opcion=0
        print("Si Desea Salir Presione 'S' Sino Ingrese Otra Opcion:")
        print("----------Menu----------")
        print("1-Volver A El Menu Principal De Opciones")
        print("2-Salir")
        print("------------------------")
        opcion = int(input("Ingrese La Opcion Deseada: "))
        if(opcion==1):
           ingreso()
        else:
           print("Hasta Luego")
           exit()
 
ingreso()