# contadores y acumuladores
total_trabajadores = 0
suma_sueldos_netos = 0
continuar = "si"

print("--- Sistema de Cálculo de Sueldos ---")

# Ciclo para ingresar trabajadores
while continuar.lower() == "si":
    # Aquí acomodé el ingreso de los datos de los empleads
    nombre = input("\nIngrese el nombre del trabajador: ")
    horas = int(input("Ingrese el número de horas trabajadas: "))
    sueldo_hora = float(input("Ingrese el sueldo por hora: "))
    
    # Aqui calculamos el sueldo base
    sueldo_base = horas * sueldo_hora
    porcentaje_aumento = 0 
    
    # Aqui podemos ver la condicion para el aumento según las horas
    if horas == 10:
        porcentaje_aumento = 0.20  # 20%
    elif horas == 15:
        porcentaje_aumento = 0.30  # 30%
    elif horas == 20:
        porcentaje_aumento = 0.15  # 15%
    elif horas > 25:
        porcentaje_aumento = 0.08  # 8%
    else:
        porcentaje_aumento = 0     # No hay aumento si no se cumplen las condiciones
        
    # Calculo final para los sueldos
    monto_aumento = sueldo_base * porcentaje_aumento
    sueldo_neto = sueldo_base + monto_aumento
    
    # Imprimimos resultados individuales
    print(f"\nResultados para {nombre}:")
    print(f"Aumento a pagar: ${monto_aumento}")
    print(f"Sueldo neto cobrado: ${sueldo_neto}")
    
    # Actualizo l total en datos generales
    total_trabajadores += 1
    suma_sueldos_netos += sueldo_neto
    
    # Preguntar si deseamos continuar 
    continuar = input("\n¿Deseas ingresar otro trabajador? (si/no): ")

# --- Detalle Final del informe ---
print("\n" + "="*30)
print("RESUMEN FINAL")
print(f"Total de trabajadores ingresados: {total_trabajadores}")
print(f"Monto total de sueldos netos: ${suma_sueldos_netos:.2f}")
print("="*30)