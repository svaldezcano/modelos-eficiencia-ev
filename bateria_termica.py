#informacion del fabricante
m=40
cp=1000
rit=0.1
i=float(input("Cuanta corriente tiene la bateria en Amperes:"))
t=float(input("Cuanto tiempo demoro :"))
T0=float(input("Que temperatura tenia al inicio:"))
def simular_temperatura_bateria(corriente, resistencia, tiempo, masa, temperatura_0, calor_especifico):
	i=corriente
	rit=resistencia
	t=tiempo
	m=masa
	cp=calor_especifico
	T0=temperatura_0
	q=pow(i,2)*rit*t
	d=q/(m*cp)
	T1=T0+d
	return T1
f=simular_temperatura_bateria(i,rit,t,m,T0,cp)
print("La temperatura que alcanza la bateria es:",f)
