

def obs1(l):
    l2=[]
    juego_fi="no"
    juego_fo="no"
    juego_va="no"
    d4="0"
    d5="0"
    d6="0"

    d1=input("Identificador de Jugador(ID): ")
    d2=input("Nombre jugador: ")
    d3=input("Apellido jugador: ")

    #d1 = dato 1
    while True:
        obs2=input(f"""
    que juego participas: 
                1)fifa      [{juego_fi}]
                2)fornite   [{juego_fo}]
                3)valorant  [{juego_va}]

                0)solo esos
    """)
        if obs2 == "1":
            juego_fi="si"
        elif obs2 == "2":
            juego_fo = "si"
        elif obs2 == "3":
            juego_va="si"
        elif obs2 == "0":
            break
        else:
            print("Error no existe esa alternativa")
    if juego_fi=="si":
        d4=input("Puntaje Fifa: ")
    if juego_fo=="si":
        d5=input("Puntaje Fornite: ")
    if juego_va=="si":
        d6=input("Puntaje Valorant: ")
    while True:
        obs2=input("""
    dificualtad: 1)principiante 
                 2)intermedio
                 3)experto
    """)
        if obs2 == "1":
            d7="principiante"
            break
        elif obs2 == "2":
            d7="intermedio"
            break
        elif obs2 == "3":
            d7="experto"
            break
        else:
            "Error: no exsite es alternativa"

    l2.append(d1.ljust(11))
    l2.append(d2.ljust(11))
    l2.append(d3.ljust(11))
    l2.append(d4.ljust(11))
    l2.append(d5.ljust(11))
    l2.append(d6.ljust(11))
    l2.append(d7.ljust(11))
    
    l.append(l2)
    
    return(l)
    


def obs2(l):
    print("ID        |Nombre    |Apellido  |P.Fifa    |P.Fornite |P.Valorant|Dificultad")
    for i in range(len(l)):
        for x in range(len(l[i])):
            print(l[i][x], end="")
        print()


def obs3(l):
    with open("documento.txt","w") as file:
        for i in l:
            file.writelines(i)


