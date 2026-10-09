import csv

# Abre el archivo en modo lectura ('r')
with open('telemetria_motor.csv', mode='r') as archivo:
    lector = csv.reader(archivo)
    
    # Salta la primera fila porque contiene texto (los nombres de las columnas)
    next(lector) 
    
    # Lee los datos línea por línea
    for fila in lector:
        # Extrae cada posición de la lista y la convierte en un número operable
        tiempo = float(fila[0])
        t_alta = float(fila[1])
        t_baja = float(fila[2])
        q_in = float(fila[3])
        trabajo = float(fila[4])
        
        # --------------------------------------------------------
        # TU TRABAJO INICIA AQUÍ:
        # Usa t_alta, t_baja, q_in y trabajo para calcular:
        # 1. Eficiencia máxima de Carnot (Ideal)
	ef_carnot=1-t_baja/t_alta
        # 2. Eficiencia real del motor
	ef_real=trabajo/q_in
        # 3. Imprime si la fila de datos representa un motor
        #    Real, Ideal, o Imposible (violación a la 2da Ley)
	if ef_real<ef_carnot:
		print(f"El proceso {int(tiempo)} es posible.")
	elif ef_real==ef_carnot:
		print(f"El proceso {int(tiempo)} es ideal.")
	else:
		print(f"El proceso {int(tiempo)} es imposible.")
        # --------------------------------------------------------
