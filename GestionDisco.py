from tkinter import *
root = Tk()
root.title("Menu")

# Canva
canvas = Canvas(root, height=150, width=200)
canvas.pack()

frame = Frame(root)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
#creando para FCFFS
ventana=Toplevel()
ventana.title("Politica FCFS")
canvas1 = Canvas(ventana, height=500, width=800)
frame1=Frame(ventana)
frame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
#creando para SSTF
ventana1=Toplevel()
ventana1.title("Politica SSTF")
canvas0 = Canvas(ventana1, height=500, width=800)
frame0=Frame(ventana1)
frame0.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
#titulo
label = Label(frame, text="    GESTION DE DISCO   ")
label.grid(row=1, column=1, sticky=W+E)
#input
Politica = Entry(frame)
Politica.grid(row=2, column=1,sticky=W+E)
Politica.focus()
# Button
button = Button(frame, text="Seleccionar Politica",command=lambda:newventana(Politica.get()))
button.grid(row=3, column=1, sticky=W+E)
pFCFS=[['po',0,15],['p1',0,28],['p2',0,60]]
pSSTF=[['po',0,32],['p1',0,20],['p2',0,7],['p4',0,60]]
Peticiones=pSSTF
OrdenAuxiliar=Peticiones
tamaño=0
Uini=30
Uact=Uini
def addPet(name,tlleg,pos,frame):
    global Peticiones
    Peticiones.append([name,int(tlleg),int(pos)])
    mostrarPeticiones(frame)
def addtdisco(tam,frame):
    global tamaño
    tamaño=tam
    mostrardisco(frame)
def addPosini(pos,frame):
    global Uini
    Uini=pos
    mostrarpos(frame)
def mostrarPeticiones(frame):
    global Peticiones
    listbox=Listbox(frame,width=10, height=5)
    listbox.grid(row=6, column=0, columnspan=4, sticky=W+E)
    
    for x in Peticiones:
        listbox.insert(END, x)
def mostrardisco(frame):
    label = Label(frame, text="tamaño actual: ")
    label.grid(row=4, column=5)

    label = Label(frame, text=tamaño)
    label.grid(row=5, column=5)
def mostrarpos(frame):
    label = Label(frame, text="Pos Inicial: ")
    label.grid(row=4, column=6)

    label = Label(frame, text=Uini)
    label.grid(row=5, column=6)
def newventana(pol):
    if pol == "FCFS":
        FCFS()
    elif pol == "SSTF":
        SSTF()
    elif pol == "SCAN":
        SCAN()
    elif pol == "LOOK":
        LOOK()
    elif pol == "CSCAN":
        CSCAN()
    elif pol == "CLOOK":
        CLOOK()
def mostarGrafico(frame):
    global OrdenAuxiliar
    global Uini
    global Uact
    #titulo
    label = Label(frame, text="    cuadro de Tiempos de Esopera  ")
    label.grid(row=5, column=5, sticky=W+E)

    listbox=Listbox(frame,width=10, height=5,)
    listbox.grid(row=6,column=5, columnspan=4, sticky=W+E)
    listbox.insert(END,['P','TL','Pos','TE'])

    tiempo = 0

    for x in OrdenAuxiliar:
        listbox.insert(END, [x[0],x[1],x[2],abs(int(Uact)-int(x[2]))+int(tiempo)])
        tiempo += abs(int(Uact)-int(x[2]))+int(tiempo)
        Uact=x[2]
        
    for k in range(0,len(OrdenAuxiliar)):

        label1 = Label(frame0, text=OrdenAuxiliar[k][2])
        label1.grid(row=11+k, column=0+k)

def ordenar(frame):

    global OrdenAuxiliar

    elementos = OrdenAuxiliar
    #algoritmo de ordenamiento
    numero = len(elementos)
    i= 0
    while (i < numero):
        j = i
        while (j < numero):
            if(elementos[i][1] > elementos[j][1]):
                temp = elementos[i]
                elementos[i]= elementos[j]
                elementos[j] = temp
            j= j+1
        i=i+1
    OrdenAuxiliar = elementos

    mostarGrafico(frame)
def FCFS():
    canvas1.pack()

    label = Label(frame1, text="Ingrese La Peticion")
    label.grid(row=0, column=1, sticky=W+E)

    # Name 
    label = Label(frame1, text="Nombre")
    label.grid(row=1, column=0)

    entry_name = Entry(frame1)
    entry_name.grid(row=1, column=1)
    entry_name.focus()

    # Tiempo de llegada 
    label = Label(frame1, text="T-llegada")
    label.grid(row=2, column=0)

    entry_tllegada = Entry(frame1)
    entry_tllegada.grid(row=2, column=1)
    entry_tllegada.focus()

    # POS
    label = Label(frame1, text="Ubicacion en Disco")
    label.grid(row=3, column=0)

    entry_pos = Entry(frame1)
    entry_pos.grid(row=3, column=1)



    # Button
    button = Button(frame1, text="Entrar la Peticion",command=lambda:addPet(
        entry_name.get(),
        entry_tllegada.get(),
        entry_pos.get(),
        frame1
    ))
    button.grid(row=4, column=1, sticky=W+E)

    mostrarPeticiones(frame1)

    #definir tamaño de disco


    label = Label(frame1, text="n pistas de disco")
    label.grid(row=0, column=5)

    TDisco = Entry(frame1)
    TDisco.grid(row=1, column=5)
    TDisco.focus()

    # Button
    button = Button(frame1, text="Definir Pistas",command=lambda:addtdisco(
        TDisco.get(),
        frame1
    ))
    button.grid(row=2, column=5, sticky=W+E)

    label = Label(frame1, text="Ubicacion Inicial")
    label.grid(row=0, column=6)

    npistas = Entry(frame1)
    npistas.grid(row=1, column=6)
    npistas.focus()

    # Button
    button = Button(frame1, text="Definir Ubicacion",command=lambda:addPosini(
        npistas.get(),
        frame1
    ))
    button.grid(row=2, column=6, sticky=W+E)

    # Button
    button = Button(frame1, text="Aplicar Politica FCFS",command=lambda:ordenar(frame1))
    button.grid(row=4, column=3, sticky=W+E)
def SSTF():
    canvas0.pack()

    label = Label(frame0, text="Ingrese La Peticion")
    label.grid(row=0, column=1, sticky=W+E)

    # Name 
    label = Label(frame0, text="Nombre")
    label.grid(row=1, column=0)

    entry_name = Entry(frame0)
    entry_name.grid(row=1, column=1)
    entry_name.focus()

    # Tiempo de llegada 
    label = Label(frame0, text="T-llegada")
    label.grid(row=2, column=0)

    entry_tllegada = Entry(frame0)
    entry_tllegada.grid(row=2, column=1)
    entry_tllegada.focus()

    # POS
    label = Label(frame0, text="Ubicacion en Disco")
    label.grid(row=3, column=0)

    entry_pos = Entry(frame0)
    entry_pos.grid(row=3, column=1)



    # Button
    button = Button(frame0, text="Entrar la Peticion",command=lambda:addPet(
        entry_name.get(),
        entry_tllegada.get(),
        entry_pos.get(),
        frame0
    ))
    button.grid(row=4, column=1, sticky=W+E)

    mostrarPeticiones(frame0)

    #definir tamaño de disco


    label = Label(frame0, text="n pistas de disco")
    label.grid(row=0, column=5)

    TDisco = Entry(frame0)
    TDisco.grid(row=1, column=5)
    TDisco.focus()

    # Button
    button = Button(frame0, text="Definir Pistas",command=lambda:addtdisco(
        TDisco.get(),
        frame0
    ))
    button.grid(row=2, column=5, sticky=W+E)

    label = Label(frame0, text="Ubicacion Inicial")
    label.grid(row=0, column=6)

    npistas = Entry(frame0)
    npistas.grid(row=1, column=6)
    npistas.focus()

    # Button
    button = Button(frame0, text="Definir Ubicacion",command=lambda:addPosini(
        npistas.get(),
        frame0
    ))
    button.grid(row=2, column=6, sticky=W+E)

    # Button
    button = Button(frame0, text="Aplicar Politica SSTF",command=lambda:ordenar(frame0))
    button.grid(row=4, column=3, sticky=W+E)
def SCAN():
    ventana2=Toplevel()
    canvas2 = Canvas(ventana2, height=500, width=800)
    canvas2.pack()
    ventana2.title("Politica SCAN")
def LOOK():
    ventana3=Toplevel()
    canvas3 = Canvas(ventana3, height=500, width=800)
    canvas3.pack()
    ventana3.title("Politica LOOK")
def CSCAN():
    ventana4=Toplevel()
    canvas4 = Canvas(ventana4, height=500, width=800)
    canvas4.pack()
    ventana4.title("Politica C-SCAN")
def CLOOK():
    ventana5=Toplevel()
    canvas5 = Canvas(ventana5, height=500, width=800)
    canvas5.pack()
    ventana5.title("Politica C-LOOK")

root.mainloop()
