






def over_the_road(numero_casa, longitud_casas):
    casas_izquierda = []
    casas_derecha = []
    c = 1
    while True:
        if c % 2 == 0:
            casas_derecha.append(c)
        else:
            casas_izquierda.append(c)
        if len(casas_derecha) == longitud_casas and len(casas_izquierda) == longitud_casas:
            break
        
        c += 1

    casas_derecha.sort(reverse=True)



    if numero_casa % 2 == 0:
        indice = casas_derecha.index(numero_casa)
        print(casas_izquierda)    
    else:
        indice = casas_izquierda.index(numero_casa)
        print(casas_izquierda[indice])

over_the_road(3, 5)
over_the_road(1, 3)   
over_the_road(3, 3)   
  