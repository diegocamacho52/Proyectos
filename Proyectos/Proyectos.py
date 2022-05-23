import os
import time
os.system('cls')



def bingo():
    

        from os import sep
        allnum=[]
        for item in range (1,76):
            allnum.append(item)
        B_list=[]
        I_list=[]
        N_list=[]
        G_list=[]
        O_list=[]
        B=[]
        I=[]
        N=[]
        G=[]
        O=[]
        condicion=True
        print("\t\t\t\t\t\t╭┓┏╮┏━━━━━┓╭┓┏╮\n\t\t\t\t\t\t┃┃┃┃┃▔╲╳╱▔┃┃┃┃┃\n\t\t\t\t\t\t┃┗┛┃╰╮▋▂▆╭╯┃┗┛┃\n\t\t\t\t\t\t╰┳┳╯╭┛▕▂▏┗╮╰┳┳╯\n\t\t\t\t\t\t╭╯┃╱┃▇▅▃▆▉┃╳┃╰╮\n\t\t\t\t\t\t┣╭╯╳┃┏┈┈┈┓┃╱╰╮┫\n\t\t\t\t\t\t┣╰━━┫┊╋▇╳┊┣━━╯┫\n\t\t\t\t\t\t╰┻┻┻┫┗┈┈┈┛┣┻┻┻╯")
        print("\t\t\t\t\t\t Bingo juego")
        print()
        for allnum in range(1,16):
            B_list.append(allnum)
        print("B=>",*B_list,sep=" , ")
        for allnum in range(16,31):
            I_list.append(allnum)
        print("I=>",*I_list,sep=" , ")
        for allnum in range(31,46):
            N_list.append(allnum)
        print("N=>",*N_list,sep=" , ")
        for allnum in range(46,61):
            G_list.append(allnum)
        print("G=>", *G_list,sep=" , ")
        for allnum in range(61,76):
            O_list.append(allnum)
        print("O=>", *O_list,sep=" , ")
        print()
        while condicion==True:
            draw=input ("¿Quieres elegir un número de bingo (Y/N)?")
            draw= draw.capitalize()
            if draw=='Y':

                import random
            allnum=[]
            for item in range(1,76):
                allnum.append(item)

            selecionum=random.choice(allnum)
            print()

            if selecionum>= 1 and selecionum<=9:
                B.append(selecionum)
                if selecionum in B_list:
                    B_list.remove(selecionum)
                else:
                    print("el mismo número ha sido elegido")
                    draw=input("¿Quiere escoger un numeros de bingo(Y/N)?")
                
                print("B=>",*B_list,sep=" , ")
                print("I=>",*I_list,sep=" , ")
                print("N=>",*N_list,sep=" ," )
                print("G=>",*G_list,sep=",")
                print("O=>",*O_list,sep=",")

                print("\nselecion de numero")
                print("B=>"+str(B)[1:-1],sep=" , ")
                print("I=>"+str(I)[1:-1],sep=" , ")
                print("N=>"+str(N)[1:-1],sep=" , ")
                print("G=>"+str(G)[1:-1],sep=" , ")
                print("O=>"+str(O)[1:-1],sep=" , ")
                print()
                print("Quieres elegir un numero:B-O"+str(selecionum))
                print()
                input("presione la tecla enter para continuar..")
                print()
            if selecionum>= 10 and selecionum<=15:
                B.append(selecionum)
                if selecionum in B_list:
                    B_list.remove(selecionum)
                else:
                    print("el mismo número ha sido elegido")
                    draw=input("¿Quiere escoger un numeros de bingo(Y/N)?")
                
                print("B=>", *B_list,sep=" , ")
                print("I=>", *I_list,sep=" , ")
                print("N=>", *N_list,sep=" , ")
                print("G=>", *G_list,sep=" , ")
                print("O=>", *O_list,sep=" , ")

                print("\nselecion de numero")
                print("B=>"+str(B)[1:-1],sep=" , ")
                print("I=>"+str(I)[1:-1],sep=" , ")
                print("N=>"+str(N)[1:-1],sep=" , ")
                print("G=>"+str(G)[1:-1],sep=" , ")
                print("O=>"+str(O)[1:-1],sep=" , ")
                print()
                print("Quieres elegir un numero:B-"+str(selecionum))
                print()
                input("presione la tecla enter para continuar..")
                print()
            if selecionum>=16 and selecionum<=30:
                I.append(selecionum)
                if selecionum in I_list:
                    I_list.remove(selecionum)
                else:
                    print("el mismo número ha sido elegido")
                    draw=input("¿Quiere escoger un numeros de bingo(Y/N)?")
                
                print("B=>",*B_list,sep=" , ")
                print("I=>",*I_list,sep=" , ")
                print("N=>",*N_list,sep=" , ")
                print("G=>",*G_list,sep=" , ")
                print("O=>",*O_list,sep=" , ")

                print("\nselecion de numero")
                print("B=>"+str(B)[1:-1],sep=" , ")
                print("I=>"+str(I)[1:-1],sep=" , ")
                print("N=>"+str(N)[1:-1],sep=" , ")
                print("G=>"+str(G)[1:-1],sep=" , ")
                print("O=>"+str(O)[1:-1],sep=" , ")
                print()
                print("Quieres elegir un numero:I-"+str(selecionum))
                print()
                input("presione la tecla enter para continuar..")
                print()
            if selecionum>=31 and selecionum<=45:
                N.append(selecionum)
                if selecionum in N_list:
                    N_list.remove(selecionum)
                else:
                    print("el mismo número ha sido elegido")
                    draw=input("¿Quiere escoger un numeros de bingo(Y/N)?")
                
                print("B=>",*B_list,sep=" , ")
                print("I=>",*I_list,sep="  ,")
                print("N=>",*N_list,sep=" , ")
                print("G=>",*G_list,sep=" , ")
                print("O=>",*O_list,sep=" , ")

                print("\nselecion de numero")
                print("B=>"+str(B)[1:-1],sep=" , ")
                print("I=>"+str(I)[1:-1],sep=" , ")
                print("N=>"+str(N)[1:-1],sep=" , ")
                print("G=>"+str(G)[1:-1],sep=" , ")
                print("O=>"+str(O)[1:-1],sep=" , ")
                print()
                print("Quieres elegir un numero:N-"+str(selecionum))
                print()
                input("presione la tecla enter para continuar..")
                print()
            if selecionum>=46 and selecionum<=60:
                G.append(selecionum)
                if selecionum in G_list:
                    G_list.remove(selecionum)
                else:
                    print("el mismo número ha sido elegido")
                    draw=input("¿Quiere escoger un numeros de bingo(Y/N)?")
                
                print("B=>",*B_list,sep=" , ")
                print("I=>",*I_list,sep=" , ")
                print("N=>",*N_list,sep=" , ")
                print("G=>",*G_list,sep=" , ")
                print("O=>",*O_list,sep=" , ")

                print("\nselecion de numero")
                print("B=>"+str(B)[1:-1],sep=" , ")
                print("I=>"+str(I)[1:-1],sep=" , ")
                print("N=>"+str(N)[1:-1],sep=" , ")
                print("G=>"+str(G)[1:-1],sep=" , ")
                print("O=>"+str(O)[1:-1],sep=" , ")
                print()
                print("Quieres elegir un numero:G-"+str(selecionum))
                print()
                input("presione la tecla enter para continuar..")
                print()
            if selecionum>=61 and selecionum<=75:
                O.append(selecionum)
                if selecionum in O_list:
                    O_list.remove(selecionum)
                else:
                    print("el mismo número ha sido elegido")
                    draw=input("¿Quiere escoger un numeros de bingo(Y/N)?")
                
                print("B=>",*B_list,sep=" , ")
                print("I=>",*I_list,sep=" , ")
                print("N=>",*N_list,sep=" , ")
                print("G=>",*G_list,sep=" , ")
                print("O=>",*O_list,sep=" , ")

                print("\nselecion de numero")
                print("B=>"+str(B)[1:-1],sep=" , ")
                print("I=>"+str(I)[1:-1],sep=" , ")
                print("N=>"+str(N)[1:-1],sep=",")
                print("G=>"+str(G)[1:-1],sep=",")
                print("O=>"+str(O)[1:-1],sep=",")
                print()
                print("Quieres elegir un numero:O-"+str(selecionum))
                print()
                input("presione la tecla enter para continuar..")
                print()
            elif draw=='N':
                condicion=False

            draw2=input("¿Quieres poner otro bingo?(Y/N)")
            draw2=draw2.capitalize()
            print()
            if draw2 =='Y':
                print("\t\t\t\t\t\t")
                print()
                B_list.clear()
                I_list.clear()
                N_list.clear()
                G_list.clear()
                O_list.clear()
                for allnum in range(1,16):
                    B_list.append(allnum)
                print("B=>",B_list,sep=",")
                for allnum in range(16,31):
                    I_list.append(allnum)
                print("I=>",I_list,sep=",")
                for allnum in range(31,46):
                    N_list.append(allnum)
                print("N=>",N_list,sep=",")
                for allnum in range(46,61):
                    G_list.append(allnum)
                print("G=>",G_list,sep=",")
                for allnum in range(61,76):
                    O_list.append(allnum)
                print("O=>",O_list,sep=",")
                print()             

def caja():
    productos=[
        [1,'agua',1000,1000],
        [2,'cocacola',1250,3000],
        [3,'postobon',1250,2000],
        [4,'agua saborizada',500,1500],
        [5,'vive100',500,2500],
        [6,'cruazan',1,1500],
        [7,'Pan matrimonio',1,1000],
        [8,'Pan liberales',2,1200],
        [9,'pan rollo',1,500],
        [10,'mogolla',1,200],
        [11,'mani salado',1,1000],
        [12,'manimoto',1,1000],
        [13,'mani TOTO',1,3000],
        [14,'mani crack',1,800],
        [15,'mani especial',1,2000],
        [16,'oreo',1,1000],
        [17,'festival',1,1000],
        [18,'milo',1,1200],
        [19,'galleta mermelada',1,3000],
        [20,'tosh',1,1300],
        [21,'colgate',350,2500],
        [22,'jabon jhonson',1,3000],
        [23,'cepillo de diente',1,1500],
        [24,'Listerine',1000,15000],
        [25,'gillete',1,3000],
        [26,'limpido',1000,5000],
        [27,'fab fab',500,3000],
        [29,'suavitel',250,1500],
        [30,'Blanqueador yes',250,1000],
        [31,'cuaderno de 100hojas',1,2000],
        [32,'hojas de block',1,4500],
        [33,'lapizero negro',1,1500],
        [34,'cuaderno de 50hojas',1,1000],
        [35,'lapiz negro',1,800],
        [36,'carne de res',500,12000],
        [37,'carne de cerdo',500,9500],
        [38,'pollo',500,8500],
        [39,'mojarra roja',500,6000],
        [40,'Salmon',500,8000],
        [41,'queso costeño',500,7000],
        [42,'queso mozarella',1,1200],
        [43,'queso parmezano rallado',1,20000],
        [44,'queso crema',500,5000],
        [45,'arroz',1,1000],
        [46,'huevo',1,500],
        [47,'aceite',500,2000],
        [48,'platano verde',1,1500],
        [49,'guineo verde',1,200],
        [50,'platano maduro',1,2000],
    ]

    compra=[]
    acum=0
    os.system('cls')
    x=True
    while x==True:
        try:
            menuprincipal=int(input('Bienvenido a SuperTiendala13:  \n 1-Ver Productos \n 2-Productos seleccionados \n 3-Eliminar Producto \n 4-Pagar productos \n 0-Salir \n-->'))
            if menuprincipal==1:
                control=True
                print("--------------PRODUCTOS--------------")
                for i in productos:
                    print(f"{i[1].title()}:{i[2]} - Precio: {i[3]} - Codigo: {i[0]}")
                while control==True:
                    cod=int(input('Ingrese el codigo\n-->'))
                    if cod>0 and cod<=50:
                        cantidad=int(input('Cantidad\n-->'))
                        if cantidad>0:
                            for i in range(len(productos)):
                                if cod in productos[i]:
                                    produc=productos[i]
                                    codigo=productos[i][0]
                                    nombre=productos[i][1]
                                    preciound=productos[i][3]
                                    preciototal=preciound*cantidad
                                    temp=[codigo,nombre,preciound,cantidad,preciototal]
                                    compra.append(temp)
                                    
                            opc=int(input('¿Quiere otro producto?\n1.Si\n2.No\n-->'))
                            if opc==1:
                                control=True
                            elif opc==2:
                                control=False

                            else:
                                print('digito erroneo')
                                opc=int(input('¿Quiere otro producto?\n1.Si\n2.No\n-->'))
                        else:
                            print('Minimo debe llevar 1 producto')
                    else:
                        print('Codigo de producto errado')
                        
            elif menuprincipal==2:
                print("----Productos Seleccionados----")
                for i in compra:
                    print(" ")
                    print(f"{i[1].title()} - Cantidad: {i[3]} - Precio: {i[4]} - Codigo: {i[0]}")
                    print(" ")

            elif menuprincipal==3:
                control=True
                print("----Eliminador de Productos----")
                for i in compra:
                    print(f"{i[1].title()} - Cantidad: {i[3]} - Precio: {i[4]} - Codigo: {i[0]}")
                while control==True:
                    n=int(input('Ingrese el codigo del producto a eliminar \n--> '))
                    for i in range(len(compra)):
                        if n==compra[i][0]:
                            compra.remove(compra[i])
                            pre=int(input('¿Quiere seguir removiendo productos?\n1.Si\n2.No\n-->'))
                            if pre==1:
                                control=True
                            elif pre==2:
                                control=False
                            else:
                                print("Codigo erroneo")
                                pre=int(input('¿Quiere seguir removiendo productos?\n1.Si\n2.No\n-->'))
                                
            elif menuprincipal==4:
                os.system('cls')
                print("----Total----")
                acu=0
                for i in range (len(compra)):
                    acu=acu+compra[i][4]
                for i in range (len(compra)):
                    print(compra[i])
                print(acu)
                x=False
                time.sleep(2)

                
            elif menuprincipal==0:
                print("---- Salir ----")
                x=False
            else:
                print("\n----Por favor digita una opcion correcta----")
        except:
            os.system('cls')

def millonario():

    os.system("cls")
    condicion=True
    recom=0
    while condicion==True:
        
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Romeo\nB) Macbeth \nC) Hamlet \nD) Darren ")
        pregunta_1=input("¿Cuál de estos nombres no aparece en el título de una obra de Shakespeare? --> ").lower()
        time.sleep(2)

        A="Romeo"
        B="Macbeth"
        C="Hamlet"
        D="Darren"   

        if pregunta_1=="d":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Escocia \nB) Gales \nC) Estados Unidos \nD) Irlanda")
        pregunta_2=input("¿Cuál es el lugar de origen del whisky escocés? --> ").lower()


        A="Escocia"
        B="Gales"
        C="Estados Unidos"
        D="Irlanda"   

        if pregunta_2=="a":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) 3 \nB) 2 \nC) 8 \nD) 18")
        pregunta_3=input("¿Cuantas caras tiene un octaedro? --> ").lower()


        A="3"
        B="2"
        C="8"
        D="18"   

        if pregunta_3=="c":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) El Valle de la Muerte  \nB) Los Grandes Lagos  \nC) El Gran Cañón  \nD) El jacuzzi de Mark Zuckerberg")
        pregunta_4=input("¿Qué parte importante de la topografía de Estados Unidos comprende aproximadamente un 20% del agua dulce de la Tierra? --> ").lower()


        A="El Valle de la Muerte"
        B="Los Grandes Lagos"
        C="El Gran Cañón"
        D="El jacuzzi de Mark Zuckerberg"   

        if pregunta_4=="b":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break
                
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Cardo \nB) Rosa \nC) Puerro \nD) Trebol\nE) Retirarte")
        print()
        print("Deseas retirarte?")
        pregunta_5=input("¿Qué planta es el símbolo nacional de Irlanda? --> ").lower()


        A="Cardo"
        B="Rosa"
        C="Puerro"
        D="Trebol"
        E="Retirarte"   

        if pregunta_5=="d":  
            print("Correcto")
        elif pregunta_5=="e":
            print("Has ganado $", recom-50000)
            condicion=False
            time.sleep(2)
            break
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) De un ataque al corazón  \nB) De tuberculosis \nC)  De insuficiencia renal aguda \nD) De un cáncer estomacal")
        pregunta_6=input("¿De qué murió el compositor Chopin? --> ").lower()


        A="De un ataque al corazón"
        B="De tuberculosis"
        C="De insuficiencia renal aguda"
        D="De un cáncer estomacal"   

        if pregunta_6=="b":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Ginger Rogers \nB) Deanna Durbin \nC) Doris Day \nD) Judy Garland ")
        pregunta_7=input("¿Qué famosa estrella musical fue conocida como Baby Frances Gumm en la fase inicial de su carrera? --> ").lower()


        A="Ginger Rogers"
        B="Deanna Durbin"
        C="Doris Day"
        D="Judy Garland"   

        if pregunta_7=="d":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Enrique IV \nB) Carlos III \nC) Luis XII \nD) Francisco I")
        pregunta_8=input("¿En la corte de qué rey pasó Leonardo Da Vinci los dos últimos años de su vida? --> ").lower()


        A="Enrique IV"
        B="Carlos III"
        C="Luis XII"
        D="Francisco I"   

        if pregunta_8=="d":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Síndrome de Proust \nB) Síndrome de Jerusalén \nC) Síndrome de Stendhal \nD) Síndrome de Beckett ")
        pregunta_9=input("¿La gente que tiene una reacción física importante hacia el arte hermoso, ¿qué tipo de síndrome sufre? --> ").lower()


        A="Síndrome de Proust"
        B="Síndrome de Jerusalén"
        C="Síndrome de Stendhal"
        D="Síndrome de Beckett"   

        if pregunta_9=="c":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Calico Jack \nB) Barbanegra \nC) Bartholomew Roberts \nD) Capitán Kidd\nE) Retirarst ")
        print()
        print("Deseas retirarte?")
        pregunta_10=input("¿En 1718, ¿qué pirata murió en una batalla en la costa del lugar ahora conocido como Carolina del Norte? --> ").lower()


        A="Calico Jack"
        B="Barbanegra"
        C="Bartholomew Roberts"
        D="Capitán Kidd"
        E="Retirarte"   

        if pregunta_10=="b":  
            print("Correcto")
        elif pregunta_5=="e":
            print("Has ganado $", recom-50000)
            condicion=False
            time.sleep(2)
            break
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Gibberish \nB) Jabberwocky \nC) Twaddle \nD) Gobbledygook ")
        pregunta_11=input("¿Cuál es el título del poema de Lewis Carroll compuesto por palabras sinsentido?? --> ").lower()


        A="Gibberish"
        B="Jabberwocky"
        C="Twaddle"
        D="Gobbledygook"   

        if pregunta_11=="b":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Tienes un ataque de pánico \nB) Recuerdas un nombre \nC) Entiendes una broma \nD) Escuchas música")
        pregunta_12=input("¿Los neurólogos creen que la corteza prefrontal del cerebro se activa cuando haces qué? --> ").lower()


        A="Tienes un ataque de pánico"
        B="Recuerdas un nombre"
        C="Entiendes una broma"
        D="Escuchas música"   


        if pregunta_12=="c":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Fin \nB) Conclusión \nC) Final \nD) Acabó")
        pregunta_13=input("¿Qué palabra aparece tradicionalmente en la pantalla al terminar un largometraje? --> ").lower()


        A="Fin"
        B="Conclusión"
        C="Final"
        D="Acabó"   

        if pregunta_13=="a":  
            print("Correcto")
        else:
            m_error() 
            time.sleep(2)
            condicion=False
            break   
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Vladimir Titov \nB) Michael Collins \nC) Gus Grissom \nD) Yuri Gagarin")
        pregunta_14=input("¿Quién fue el primer hombre en viajar dos veces al espacio? --> ").lower()


        A="Vladimir Titov"
        B="Michael Collins"
        C="Gus Grissom"
        D="Yuri Gagarin"   

        if pregunta_14=="c":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Baby drizzle \nB) Baby shower \nC) Baby downpour \nD) Baby deluge\nE) Retirarte")
        print("")
        print("Deseas retirarte?")
        pregunta_15=input("¿Qué nombre tiene tradicionalmente la fiesta que se hace a una mujer que espera un bebé? --> ").lower()


        A="Baby drizzle"
        B="Baby shower"
        C="Baby downpour"
        D="Baby deluge"
        E="Retirarte"   

        if pregunta_15=="b":  
            print("Correcto")
        elif pregunta_5=="e":
            print("Has ganado $", recom-50000)
            condicion=False
            time.sleep(2)
            break
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Un pretzel \nB) Una menta \nC) Una foto de Wolf Blitzer \nD) Una manzana")
        pregunta_16=input("En los hoteles elegantes, ¿qué snack suele dejarse sobre las almohadas? --> ").lower()


        A="Un pretzel"
        B="Una menta"
        C="Una foto de Wolf Blitzer"
        D="Una manzana"   

        if pregunta_16=="b":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Madrid \nB) Dresden \nC) París \nD) Roma")
        pregunta_17=input("Existen tres ciudades europeas que preservan manuscritos originales de la civilización maya. ¿Cuál de estas ciudades no los tiene? --> ").lower()


        A="Madrid"
        B="Dresden"
        C="París"
        D="Roma"   

        if pregunta_17=="d":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Pelicanos \nB) Loros \nC) Tortugas \nD) Perros")
        pregunta_18=input("¿Porque animal se conoce como la isla de los pelicanos? --> ").lower()


        A="Pelicanos"
        B="Loros"
        C="Tortugas"
        D="Perros"  

        if pregunta_18=="a":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break    
        
        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) The Doors \nB) The Windows \nC) The Floors \nD) The Ceilings")
        pregunta_19=input("¿Cómo se llamaba la banda cuyo líder era Jim Morrison? --> ").lower()


        A="The Doors"
        B="The Windows"
        C="The Floors"
        D="The Ceilings"   

        if pregunta_19=="a":  
            print("Correcto")
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break

        time.sleep(3)
        os. system("cls")
        recom=recom+50000
        print('$', recom)


        print("A) Squash \nB) Voleibol \nC) Críquet \nD) Beisbol")
        pregunta_20=input('¿De qué deporte proviene la frase "bola curva" --> ').lower()


        A="Squash"
        B="Voleibol"
        C="Críquet"
        D="Beisbol"   

        if pregunta_20=="d":  
            print("Correcto")
            print()
            print('Has ganado $', recom)
        else:
            m_error()
            time.sleep(2)
            condicion=False
            break
  
def m_error():
   print('Incorrecto') 

def menu():
    condicion=True
    while True:
        try:
            os.system("cls")
            print("-- Proyectos -- \n")
            print("1. Bingo")
            print("2. Caja Registradora")
            print("3. Quien Quiere Ser Millonario")
            print('4. Exit')
            
            
            opc=int(input("-> "))    
            if opc==1:
                bingo()
            elif opc==2:
                caja()
            elif opc==3:
                millonario()
            elif opc==4:
                condicion=False
                os.system('cls')
                break                     
            else:
                m_error()
        except:
            os.system('cls')
            
def portada():
    print('⠄⠄⠄⠄⠄⠄⢴⡶⣶⣶⣶⡒⣶⣶⣖⠢⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⢠⣿⣋⣿⣿⣉⣿⣿⣯⣧⡰⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⣿⣿⣹⣿⣿⣏⣿⣿⡗⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠟⡛⣉⣭⣭⣭⠌⠛⡻⢿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⣤⡌⣿⣷⣯⣭⣿⡆⣈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣷⢛⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⢻⣷⣽⣿⣿⣿⢿⠃⣼⣧⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣛⣻⣿⠟⣀⡜⣻⢿⣿⣿⣶⣤⡀⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⢠⣤⣀⣨⣥⣾⢟⣧⣿⠸⣿⣿⣿⣿⣿⣤⡀⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⢟⣫⣯⡻⣋⣵⣟⡼⣛⠴⣫⣭⣽⣿⣷⣭⡻⣦⡀⠄\n⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⢏⣽⣿⢋⣾⡟⢺⣿⣿⣿⣿⣿⣿⣷⢹⣷⠄\n⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⢣⣿⣿⣿⢸⣿⡇⣾⣿⠏⠉⣿⣿⣿⡇⣿⣿⡆\n⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⢸⣿⣿⣿⠸⣿⡇⣿⣿⡆⣼⣿⣿⣿⡇⣿⣿⡇\n⠇⢀⠄⠄⠄⠄⠄⠘⣿⣿⡘⣿⣿⣷⢀⣿⣷⣿⣿⡿⠿⢿⣿⣿⡇⣩⣿⡇\n⣿⣿⠃⠄⠄⠄⠄⠄⠄⢻⣷⠙⠛⠋⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⡇⣿⣿⡇')
   
    print('')
   
    print('▒█▒▒▒█▒█▀▒█▒▒█▀▒█▀█▒█▀█▀█▒█▀▒\n▒█▒█▒█▒█▀▒█▒▒█▒▒█▒█▒█▒█▒█▒█▀▒\n▒█▄█▄█▒██▒█▄▒█▄▒█▄█▒█▒█▒█▒██▒')
    time.sleep(3)
    os.system('cls')
    time.sleep(2)
    menu()
portada()
