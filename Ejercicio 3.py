

def calcular_altura_promedio():
    alturas = []
  
    while True:
        altura = float(input("Ingrese una altura en metros (0 para terminar): "))
    
        if altura == 0:
            break

        alturas.append(altura)

    if alturas:
        promedio = sum(alturas) / len(alturas)
        return promedio
    else:
        return None

promedio = calcular_altura_promedio()
if promedio is not None:
    print(f"Altura promedio: {promedio:.2f} metros")
else:
    print("No se ingresaron alturas.")
