# El siguiente trabajo es un software que se encarga del funcionamiento de una máquina expendedora de snacks, con funciones extra
# como la administración de stock de la máquina, ingreso de usuarios con sus respectivos permisos e impresión de subtotales
# y totales consumidos por el usuario 
import time
# Se crean las estructuras de registro para snacks, ingreso, gestión y totales
class snacks:
    nombre_snacks=""
    cantidad_snacks=""
    precio_snacks=""
    
class ingreso:
    codigo_ingreso=""
    nombre_ingreso=""
    apellido_ingreso=""
    dni_ingreso=""
    permiso_ingreso=""
    
class gestion:
    codigo_gestion=""
    snack_gestion=""
    precio_gestion=""
    cantidad_gestion=""
    
class totales:
    codigo_totales=""
    fecha_totales=""
    horario_totales=""
    gestion_totales=""
    total_totales=""
    
    
    
def totales(opci):
    ft=open("totales.txt","r")
    line=ft.readlines()
    ft.close()
    fg=open("gestion.txt","r")
    line2=fg.readlines()
    fg.close()
    
    ft=open("totales.txt","a")
    fg=open("gestion.txt","a")
    
    print(opci)
    
    codigo_totales=str(opci)
    fecha_totales=time.strftime("%x")
    horario_totales=time.strftime("%X")
    gestion_totales=gestion.codigo_gestion
    lineas2=line2[int(opci)]
    print(lineas2)
    cantidad=0
    precio=0
    totales=0
    for lin in lineas2:
       precio=precio+float(lineas2.split(",")[2])
       cantidad=cantidad+int(lineas2.split(",")[3])
    
    
    
    
    
    print("Ticket, Imprimiendo.....")
    print(codigo_totales)
    print(fecha_totales)
    print(horario_totales)
    print(gestion_totales)
    print(cantidad)
    print(precio)
    
    ft.close()
    fg.close()
    

def gestion(ge,o):
    if(o==0):
       # El usuario admin genera un ingreso del nuevo snack, con precio y cantidad disponible
       if(ge==1):
          f = open("snacks.txt","a")
          snacks.nombre_snacks = input(str("Ingrese El Nuevo Snack: "))
          snacks.precio_snacks = input(str("Ingrese El Precio Del Snack: "))
          snacks.cantidad_snacks= input(str("Ingrese La Cantidad Del Snack: "))
          f.write(snacks.nombre_snacks+","+snacks.precio_snacks+","+snacks.cantidad_snacks+"\n")
          print("Ingreso Exitoso")
          f.close()
    
       # Se abre el archivo snacks.txt y el usuario admin puede eliminar cantidad de snack disponibles
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
       
       #El usuario admin puede ingresar y ver el listado de snacks existentes          
       if(ge==3):
          print("\033[1;35m"+"\n  -----"+'\033[0m'+'\033[1m'+"Lista De Snacks"+'\033[0m'+"\033[1;35m"+"-----"+'\033[0m')
          print("\033[;35m"+"       ═════ ══ ══════     "+'\033[0;m')
          f = open("snacks.txt")
          i = 1
          for linea in f:
              linea = linea.rstrip("\\n")
              print(" %4d: %s" %(i, linea))
              i+=1
          f.close()
                  
       #El usuario admin abre el archivo ingreso.txt y se le permite ingresar un nuevo usuario al mismo
       if(ge==4):
          f = open("ingreso.txt","a")
          ingreso.codigo_ingreso= input(str("Ingrese El Codigo Del Usuario: "))
          ingreso.nombre_ingreso = input(str("Ingrese El Nombre Del Usuario: "))
          ingreso.apellido_ingreso = input(str("Ingrese El Apellido Del Usuario: "))
          ingreso.dni_ingreso = input(str("Ingrese El Dni Del Usuario: "))
          ingreso.permiso_ingreso=input(str("Ingrese El Permiso Del Usuario: "))
          f.write(ingreso.codigo_ingreso+"   ,"+ingreso.nombre_ingreso+","+ingreso.apellido_ingreso+","+ingreso.dni_ingreso+","+ingreso.permiso_ingreso+"\n")
          print("Ingreso Exitoso")
          f.close()
        
       #Le permite al usuario admin borrar un usuario del listado 
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
       
           lineas= input("Ingrese El Codigo Del Usuario A Borrar!!: ")
           del lines[int(lineas)]
           f = open("ingreso.txt","w")
           for line in lines:
              f.write(line)
              print("Borrado Exitoso ")
           else:
              print("Error,Ingrese Nuevamente El Indice") 
           f.close()

       #Le permite al usuario admin ver el listado de los usuarios existentes
       if(ge==6):
           print("\033[1;35m"+"\n\t-----"+'\033[0m'+'\033[1m'+"Lista De Usuarios"+'\033[0m'+"\033[1;35m"+"-----"+'\033[0m')
           print("\033[;35m"+"\t     ═════ ══ ════════     "+'\033[0;m')
           f = open("ingreso.txt")
           i = 1
           for linea in f:
               linea = linea.rstrip("\\n")
               print(" %4d: %s" %(i, linea))
               i+=1
           f.close()
       if(ge==7):
            exit
        
    # Se crea un menú que le permite al usuario (cliente) ver el listado de snacks disponibles
    # y que luego seleccione el snack que desee llevar
    elif(o>0):
        if(ge==1):
            print("-----------Snacks------------")
            print("---Snack--Precio--Cantidad---")
            f = open("snacks.txt")
            i = 0
            for linea in f:
               linea = linea.rstrip("\\n")
               print(" %4d: %s" %(i, linea))
               i+=1
            f.close()
            print("-----------------------------")
            cg=input("Ingrese La Cantidad De Snacks A Llevar: ")
            if(cg=="0" or cg==""):
                ingreso()
            else:    
                fs=open("snacks.txt","r")
                fg=open("gestion.txt","r")
                lines = fs.readlines()
                lines2 = fg.readlines()
                fs.close()
                fg.close()
                
                fg=open("gestion.txt","a+")
                fs=open("snacks.txt","w")
                c=0
                while (c!=1):
                    gestion.codigo_gestion=str(o)
                    gestion.snack_gestion=input("Ingrese El Codigo Del Snack Que Desea: ")
                    lineas=lines[int(gestion.snack_gestion)]
                    gestion.precio_gestion=lineas.split(",")[1]
                    print(gestion.precio_gestion)
                    gestion.cantidad_gestion="1"
                    print(gestion.cantidad_gestion)
                    
                    snacks.nombre_snacks=lineas.split(",")[0]
                    print(snacks.nombre_snacks)
                    snacks.precio_snacks=lineas.split(",")[1]
                    print(snacks.precio_snacks)
                    snacks.cantidad_snacks=lineas.split(",")[2]
                    snacks.cantidad_snacks=int(snacks.cantidad_snacks)-1
                    snacks.cantidad_snacks=str(snacks.cantidad_snacks)
                    print(snacks.cantidad_snacks)
                    
                    #del lines[int(o)]

                    print("borrado existoso")
                    
                    for lin in lines:
                       # fs.write(snacks.nombre_snacks+","+snacks.precio_snacks+","+snacks.cantidad_snacks+"\n")
                       fs.write(lin)
                       print("regrabado tambien")
                    fs.close()  
                    
                    fg.write(gestion.codigo_gestion+","+gestion.snack_gestion+","+gestion.precio_gestion+","+gestion.cantidad_gestion+"\n")
                    fg.close()   
                    print("recontra regrabado")
                    c=1
                else:
                    print("Error,Ingrese Nuevamente El Indice") 
               
        totales(o)
            
        if(ge==3):
            exit
        
    

# Ingreso a menú de gestión o al menú para el usuario
def maquina(op): 
    ges=0
    # Se crea un menú para que el usuario admin pueda gestionar tanto los snacks
    # como también los códigos de accesso
    if(op==0):
        print("\033[0;35m"+"╔═════════"+'\033[0;m'+"Menu"+"\033[0;35m"+"═════════╗")
        print("║"+"\033[0;36m"+" 1-Ingreso De Snacks  "+'\033[0;m'+"\033[0;35m"+"║")
        print("║"+"\033[0;36m"+" 2-Egreso De Snacks   "+'\033[0;m'+"\033[0;35m"+"║")
        print("║"+"\033[0;36m"+" 3-Ver Snacks         "+'\033[0;m'+"\033[0;35m"+"║")
        print("║"+"\033[0;36m"+" 4-Ingreso De Codigos "+'\033[0;m'+"\033[0;35m"+"║")
        print("║"+"\033[0;36m"+" 5-Eliminar De Codigos"+'\033[0;m'+"\033[0;35m"+"║")
        print("║"+"\033[0;36m"+" 6-Ver Codigos        "+'\033[0;m'+"\033[0;35m"+"║")
        print("║"+"\033[0;36m"+" 7-Salir              "+'\033[0;m'+"\033[0;35m"+"║")
        print("╚══════════════════════╝"+'\033[0;m')
        ges=int(input("Favor De Ingresar Una Opcion Para Operar: "))
        gestion(ges,op)

    # Se crea un menú para que el usuario ingrese al listado de snacks disponibles
    elif(op>0):
        f=open("ingreso.txt","r")
        lines = f.readlines()
        f.close()
        
        for line in lines:
            lin="{:4.3}".format(line)
            lini="{:4.3}".format(str(op))
            if(lin==lini):
                print("linea encontrada")
                print("\033[0;35m"+"╔══════════"+'\033[0;m'+"Menu"+"\033[0;35m"+"═════════╗")
                print("║"+"\033[0;36m"+" 1-Snacks Para Llevar  "+'\033[0;m'+"\033[0;35m"+"║")  
                print("║"+'\033[0;m'+"\033[0;36m"+" 2-Salir               "+'\033[0;m'+"\033[0;35m"+"║")
                print("╚═══════════════════════╝"+'\033[0;m')
                ges=int(input("Favor De Ingresar Una Opcion Para Operar: "))
                gestion(ges,op)
        else:
            print("El Codigo Ingresado Es Incorrecto, Favor De Ingresarlo Nuevamente O Comunicarse Con RR.HH")
         
         
# Se crea el menú inicial que permite ingresar un código, el cual define si el usuario
# entra en modo gestión como admin o como cliente para retirar un snack
def ingreso():
    opcion=1
    print("▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓")
    print("\033[1;31m"+"-----Bienvenido A La Maquina De Snacks!!-----"+'\033[0;m')
    print("▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓")
    print("\n")
    while ((opcion > 0)  and (opcion!= 0)):
        print("\033[;36m"+"Favor Ingrese Su Codigo Para Empezar"+'\033[0;m')
        opcion = int(input("El Codigo Es Númerico Y Se Lo Tiene Que Proporcionar RR.HH: "))
        maquina(opcion)
    else:
        print("El Codigo Ingresado Es Incorrecto, Favor De Ingresarlo Nuevamente O Comunicarse Con RR.HH")
        opcion=0
        print("Si Desea Salir Presione 'S' Sino Ingrese Otra Opcion:")
        print("\033[0;35m"+"╔══════════════════"+'\033[0;m'+"Menu"+"\033[0;35m"+"═════════════════════╗")
        print("║"+"\033[0;36m"+" 1-Volver Al Menu Principal De Opciones    "+'\033[0;m'+"\033[0;35m"+"║")
        print("║"+'\033[0;m'+"\033[0;36m"+" 2-Salir                                   "+'\033[0;m'+"\033[0;35m"+"║")
        print("╚═══════════════════════════════════════════╝"+'\033[0;m')
        opcion = int(input("Ingrese La Opcion Deseada: "))
        if(opcion==1):
           ingreso()
        else:
           print("Hasta Luego")
           exit()
 
ingreso()