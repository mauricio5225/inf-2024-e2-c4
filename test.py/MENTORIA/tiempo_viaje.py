print("Ingrese los tiempos de cada tramo")
print("Ingrese 0 para finalizar calculos")
tiempo_total=0

while True :
    tiempo_tramo= int(input("Ingrese tiempo de viaje del tramo:  "))
    if tiempo_tramo == 0:
        break
    else :
        #tiempo_total= tiempo_total+tiempo_tramo
        tiempo_total += tiempo_tramo
tiempo_total_horas=str(tiempo_total // 60).zfill(2)
tiempo_total_minutos = str(tiempo_total % 60).zfill(2)     
print(f"Tiempo total del viaje: {tiempo_total_horas} horas : {tiempo_total_minutos} minutos")