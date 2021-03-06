# El siguiente trabajo es un software que se encarga del funcionamiento de una máquina expendedora de snacks, con funciones extra
# como la administración de stock de la máquina, ingreso de usuarios con sus respectivos permisos e impresión de subtotales
# y totales consumidos por el usuario 
import time

# Se crean las estructuras de registro con listas para snacks, ingreso, gestión y totales
nombre_snacks=""
cantidad_snacks=""
precio_snacks=""

snacks = [nombre_snacks,cantidad_snacks,precio_snacks]    

codigo_ingreso=""
nombre_ingreso=""
apellido_ingreso=""
dni_ingreso=""
permiso_ingreso=""
    
ingreso = [codigo_ingreso,nombre_ingreso,apellido_ingreso,dni_ingreso,permiso_ingreso]    

codigo_gestion=""
snack_gestion=""
precio_gestion=""
cantidad_gestion=""
    
gestion = [codigo_gestion,snack_gestion,precio_gestion,cantidad_gestion]   

codigo_totales=""
fecha_totales=""
horario_totales=""
gestion_totales=""
total_totales=""
    
totales = [codigo_totales,fecha_totales,horario_totales,gestion_totales,total_totales]    
    
    
# Se imprime el ticket con fecha, hora, código usuario, cantidad de artículos y el precio total. Se guardan los datos en archivo totales.txt
def totales(opci,cge):
    fg=open("gestion.txt","r")
    line2=fg.readlines()
    fg.close()
    
    ft=open("totales.txt","a")
    fg=open("gestion.txt","a")
    codigo_totales=str(opci)
    fecha_totales=time.strftime("%x")
    horario_totales=time.strftime("%X")
    cantidad=0
    precio=0
    cge=int(cge)
    lin=0
    for i in range(0,len(line2)):
        lin+=1
    for i in range(lin,lin-cge,-1):
       lineas2=line2[i-1]
       precio=precio+float(lineas2.split(",")[2])
       cantidad=cantidad+int(lineas2.split(",")[3])
       
    gestion_totales=lineas2.split(",")[0]
    print("\nTicket, Imprimiendo...\n\n")  
    print("┌────────────────────────────────┐")
    print("├───────"+"\033[0;31m"+"    ─ Ticket ─    "+'\033[0;m'+"───────┤")
    print("├────────────────────────────────┤")
    print("│                                │")
    print("│   "+"\033[0;36m"+"Fecha: "+'\033[0;m'+fecha_totales,"             │")
    print("│   "+"\033[0;36m"+"Hora:  "+'\033[0;m'+horario_totales,"             │")
    print("│                                │")
    print("│                                │")
    print("│  "+"\033[0;36m"+"Codigo Usuario: "+'\033[0;m'+gestion_totales,"            │")
    print("│  "+"\033[0;36m"+"Unidades:  "+'\033[0;m',cantidad,"                │")
    print("│  "+"\033[0;36m"+"Precio Total: "+'\033[0;m'+"${0:.2f}".format(precio),"         │")
    print("│                                │")
    print("│                                │")
    print("└────────────────────────────────┘")
    print("")
    total_totales=precio
    ft.write(codigo_totales+","+fecha_totales+","+horario_totales+","+gestion_totales+","+str(total_totales)+"\n")
    ft.close()
    fg.close()
    main()

def gestion(ge,o):
    if(o==0):
        # El usuario admin genera un ingreso del nuevo snack, con precio y cantidad disponible. Se guardan los datos en archivo snacks.txt
         if(ge==1):
            f = open("snacks.txt","a")
            nombre_snacks = input(str("Ingrese El Nombre Del Snack: "))
            precio_snacks = input(str("Ingrese El Precio Del Snack: "))
            cantidad_snacks= input(str("Ingrese La Cantidad Del Snack: "))
            f.write(nombre_snacks+","+precio_snacks+","+cantidad_snacks+"\n")
            print("Ingreso Exitoso")
            f.close()
            maquina(o)
    
         # Se abre el archivo snacks.txt y el usuario admin puede eliminar cantidad de snack disponibles
         if(ge==2):
            f = open("snacks.txt","r")
            i = 0
            print("")
            print("┌───────"+"\033[0;31m"+"Egreso"+'\033[0;m'+"─"+"\033[0;31m"+"De"+'\033[0;m'+"─"+"\033[0;31m"+"Snacks"+'\033[0;m'+"───────┐")
            for aline in f:
               values = aline.split()
               print("│ %4d: %s       │" %(i, values))
               i+=1
            f.close()
            print("└──────────────────────────────┘")
            print("")
          
            f = open("snacks.txt","r")
            lines = f.readlines()
            f.close()
        
            lineas= int(input("Ingrese El Número De Snack A Borrar!!: "))
            lines.pop(lineas)
            f = open("snacks.txt","w")
            for line in lines:
                f.write(line)
                print("Borrado Exitoso")
            else:
               print("Error,Ingrese Nuevamente El Indice") 
            f.close()
            maquina(o)
       
         #El usuario admin puede ingresar y ver el listado de snacks existentes          
         if(ge==3):
            print("")
            print("┌───────────────────────────┐")
            print("├─▼─▼─ "+"\033[0;31m"+"Lista De Snacks"+'\033[0;m'+" ─▼─▼─┤")
            print("├───────────────────────────┤")
            print("├────N°──Snack─Prec─Cant────┤")
            f = open("snacks.txt")
            i = 1
            for linea in f:
                linea = linea.split()
                print("│ %4d: %s    │" %(i, linea))
                i+=1
            f.close()
            print("└───────────────────────────┘")
            print("")
            maquina(o)
                  
         #Al usuario admin se le permite ingresar un nuevo usuario al sistema, agregándolo al archivo ingreso.txt
         if(ge==4):
            f = open("ingreso.txt","a")
            codigo_ingreso= input(str("Ingrese El Codigo Del Usuario: "))
            nombre_ingreso = input(str("Ingrese El Nombre Del Usuario: "))
            apellido_ingreso = input(str("Ingrese El Apellido Del Usuario: "))
            dni_ingreso = input(str("Ingrese El Dni Del Usuario: "))
            permiso_ingreso=input(str("Ingrese El Permiso Del Usuario: "))
            f.write(codigo_ingreso+"   ,"+nombre_ingreso+","+apellido_ingreso+","+dni_ingreso+","+permiso_ingreso+"\n")
            print("Ingreso Exitoso")
            f.close()
            maquina(o)
        
         #Le permite al usuario admin borrar un usuario del listado, del archivo ingreso.txt
         if(ge==5):
             f = open("ingreso.txt","r")
             i = 0
             print("")
             print("┌───────────────"+"\033[0;31m"+"Eliminar"+'\033[0;m'+"─"+"\033[0;31m"+"Usuarios"+'\033[0;m'+"───────────────┐")
             print("└──Nro──Cod─────Nom──Apell───DNI───────Tipo─────┘")
             for aline in f:
                values = aline.split()
                print(" %4d: %s" %(i, values))
                i+=1
             print("")
             f.close()

             
             f = open("ingreso.txt","r")
             lines = f.readlines()
             f.close()
       
             lineas= input("Ingrese El Codigo Del Usuario A Borrar!!: ")
             lines.pop(int(lineas))
             f = open("ingreso.txt","w")
             for line in lines:
                f.write(line)
                print("Borrado Exitoso ")
             else:
                print("Error, Ingrese Nuevamente El Indice") 
             f.close()
             maquina(o)
             
         #Le permite al usuario admin ver el listado de los usuarios existentes, en el archivo ingreso.txt
         if(ge==6):
             print("")
             print("┌───────────────────────────────────────────────┐")
             print("│"+"\033[0;35m"+"\t   -----"+'\033[0m'+"\033[0;31m"+"Lista De Usuarios"+'\033[0m'+"\033[0;35m"+"-----   \t"+'\033[0m'+"│")
             print("├───────────────────────────────────────────────┤")
             print("└──Nro──Cod─────Nom──Apell───DNI───────Tipo─────┘")
             f = open("ingreso.txt")
             i = 1
             for linea in f:
                 linea = linea.split()
                 print(" %4d: %s" %(i, linea))
                 i+=1
             f.close()
             print("")
             maquina(o)
         if(ge==7): 
             main()
        
    # Se crea un menú que le permite al usuario (cliente) ver el listado de snacks disponibles y que luego seleccione 
    # el snack que desee llevar. Se guarda en gestion.txt la compra realizada y se modifica en snacks.txt la cantidad disponible
    elif(o>0):
        if(ge==1):
            print("")
            print("\033[0;31m"+"▛─────────────────────────────▜")  
            print("├«««««««««══ "+'\033[0;m'+"Snacks"+"\033[0;31m"+" ══»»»»»»»»»┤")
            print("├──────────────────────────────┤")
            print("├────"+'\033[0;m'+"N°"+"\033[0;31m"+"──"+'\033[0;m'+"Snack"+"\033[0;31m"+"─"+'\033[0;m'+"Prec"+"\033[0;31m"+"──"+'\033[0;m'+"Cant"+"\033[0;31m"+"──────┤"+'\033[0;m')
            f = open("snacks.txt")
            i = 0
            for linea in f:
               linea = linea.split()
               print("\033[0;31m"+"│ %4d: %s       │" %(i, linea))
               i+=1
            f.close()
            print("▙─────────────────────────────▟"+'\033[0;m')
            print("")
            cg=input("Ingrese La Cantidad De Snacks A Llevar: ")
            if(cg=="0" or cg==""):
                main()
            else:    
                c=1
                while(c<=int(cg)):
                    fs=open("snacks.txt","r")
                    lines = fs.readlines()
                    fs.close()
                    
                    fg=open("gestion.txt","a+")
                    fs=open("snacks.txt","w")
                    codigo_gestion=str(o)
                    snack_gestion=input("Ingrese El Codigo Del Snack Que Desea: ")
                    lineas=lines[int(snack_gestion)]
                    precio_gestion=lineas.split(",")[1]
                    cantidad_gestion="1"
                    nombre_snacks=lineas.split(",")[0]
                    precio_snacks=lineas.split(",")[1]
                    cantidad_snacks=lineas.split(",")[2]
                    cantidad_snacks=int(cantidad_snacks)-1
                    cantidad_snacks=str(cantidad_snacks)
                    lines.pop(int(snack_gestion))
                    lines.insert(int(snack_gestion),nombre_snacks+","+precio_snacks+","+cantidad_snacks+"\n")
                    for lin in lines:
                       fs.write(lin)
                    fs.close()  
                    fg.write(codigo_gestion+","+snack_gestion+","+precio_gestion+","+cantidad_gestion+"\n")
                    fg.close()   
                    c+=1
                else:
                    totales(o,cg)    
        
            
        if(ge==2):
            main()
    else:
        main()    
    

# Ingreso a menú de gestión para el admin o al menú para el usuario
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
        print("║"+"\033[0;36m"+" 5-Eliminar Codigos   "+'\033[0;m'+"\033[0;35m"+"║")
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
                print("\033[0;35m"+"╔══════════"+'\033[0;m'+"Menu"+"\033[0;35m"+"═════════╗")
                print("║"+"\033[0;36m"+" 1-Snacks Para Llevar  "+'\033[0;m'+"\033[0;35m"+"║")  
                print("║"+'\033[0;m'+"\033[0;36m"+" 2-Salir               "+'\033[0;m'+"\033[0;35m"+"║")
                print("╚═══════════════════════╝"+'\033[0;m')
                ges=int(input("Favor De Ingresar Una Opcion Para Operar: "))
                if(ges==1):
                    gestion(ges,op)
                else:
                    main()
            else:
               print("El Codigo Ingresado Es Incorrecto, Favor De Ingresarlo Nuevamente O Comunicarse Con RR.HH")
               main()
         
# Se crea el menú inicial que permite ingresar un código, el cual define si el usuario
# entra en modo gestión como admin o como cliente para retirar un snack
def main():
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
        opcion=0
        print("Si Desea Volver Al Menu Principal?:")
        print("\033[0;35m"+"╔══════════════════"+'\033[0;m'+"Menu"+"\033[0;35m"+"═════════════════════╗")
        print("║"+"\033[0;36m"+" 1-Volver Al Menu Principal De Opciones    "+'\033[0;m'+"\033[0;35m"+"║")
        print("║"+'\033[0;m'+"\033[0;36m"+" 2-Salir                                   "+'\033[0;m'+"\033[0;35m"+"║")
        print("╚═══════════════════════════════════════════╝"+'\033[0;m')
        opcion = int(input("Ingrese La Opcion Deseada: "))
        if(opcion==1):
           opcion=0
           maquina(opcion)
        else:
           print("Hasta Luego")
           main()
 
main()