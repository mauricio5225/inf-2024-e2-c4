def calcular_tiempo_total():
    total_minutos = 0

    while True:
        tramo = input("Ingresa la duración del tramo en minutos (o 0 para terminar): ")
        minutos = int(tramo)
        if minutos == 0:
            break
        total_minutos += minutos

    horas = total_minutos // 60
    minutos_restantes = total_minutos % 60

    print(f"Tiempo total de viaje: {horas} horas y {minutos_restantes} minutos")

calcular_tiempo_total()
