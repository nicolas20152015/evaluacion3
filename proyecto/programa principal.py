import funciones as f

lista1=[]
sw=1
while sw==1:
    print("""
1. Registrar puntajes torneo
2. Listar los todos puntajes
3. Imprimir por Tipo
          
4. Salir del programa
""")

    obs=input("selecciona un numero: ")
    
    if obs=="1":
        lista1=f.obs1(lista1)
    elif obs=="2":
        f.obs2(lista1)
    elif obs=="3":
        f.obs3(lista1)
    elif obs=="4":
        sw=0
    else:
        print("Error: no existe esa alternativa")

