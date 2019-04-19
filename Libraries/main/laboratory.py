import statistics
from custom_functions import temperature_methods

print("buenas")
Santander = [20, 19, 18, 17, 14, 15, 16, 15, 14, 18, 17, 18]
Guajira = [30, 29, 27, 31, 34, 35, 31, 34, 32, 33, 31, 30]
Narigno = [35, 34, 35, 31, 34, 35, 35, 34, 31, 32, 33, 30]
print("Punto A")
prom_1=temperature_methods.promedio_temperature(Santander)
prom_2=temperature_methods.promedio_temperature(Narigno)
prom_3=temperature_methods.promedio_temperature(Guajira)
print("El promedio de las temperaturas en Santander es: ",prom_1)
print("El promedio de las temperaturas en Narigno es: ",prom_2)
print("El promedio de las temperaturas en Guajira es: ",prom_3)

print("Punto B")
nacional=[20, 19, 18, 17, 14, 15, 16, 15, 14, 18, 17, 18,30, 29, 27, 31, 34, 35, 31, 34, 32, 33, 31, 30,35, 34, 35, 31, 34, 35, 35, 34, 31, 32, 33, 30]
prom_nacional=temperature_methods.promedio_temperature(nacional)
print("El promedio de temperatura nacionalmente es: ",prom_nacional)


print("Punto C")
mess=("enero","febrero","marzo","abril","mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
cal_1=temperature_methods.temperature_best(Santander)
cal_2=temperature_methods.temperature_best(Narigno)
cal_3=temperature_methods.temperature_best(Guajira)
mes_1=Santander.index(calcul_1)
mes_2=Narigno.index(calcul_2)
mes_3=Guajira.index(calcul_3)
print("El mes mas caliente de Santander es",mess[mes_1],"con un valor de: ",calcul_1)
print("El mes mas caliente de Narigno es",mess[mes_2],"con un valor de: ",calcul_2)
print("El mes mas caliente de Guajira es",mess[mes_3],"con un valor de: ",calcul_3)


print("Punto D")
cal_T=[cal_1,cal_2,cal_3]
prom_cal=temperature_methods.promedio_temperature(cal_T)
print("El promedio de la temperatura en los 3 departamentos es:" ,prom_cal)

print("Punto E")
prom_T=[prom_1,prom_2,prom_3]
t_prom=temperature_methods.temperature_best(prom_T)
print("El promedio mas caliente de los 3 departamentos es: ",t_prom)

print("Punto F")
d={0:"enero",1:"febrero",2:"marzo",3:"abril",4:"mayo",5:"junio",6:"julio",7:"agosto",8:"septiembre",9:"Octubre",10:"Noviembre",11:"Diciembre",12:"enero",13:"febrero",14:"marzo",15:"abril",16:"mayo",17:"junio",18:"julio",19:"agosto",20:"septiembre",21:"Octubre",22:"Noviembre",23:"Diciembre",24:"enero",25:"febrero",26:"marzo",27:"abril",28:"mayo",29:"junio",30:"julio",31:"agosto",32:"septiembre",33:"Octubre",34:"Noviembre",35:"Diciembre"}
mayord=temperature_methods.temperature_best(cal_T)
depa=["Santander","Narigno","Guajira"]
posi=cal_T.index(mayord)
mes_f=nacional.index(mayord)
print("La temperatura mas caliente en todo el ano fue de ",mayord,"encontrada en el departamento de ",depa[posi],"en el mes de ",d[mes_f])

print("Punto G")
s1=statistics.stdev(Santander)
s2=statistics.stdev(Narigno)
s3=statistics.stdev(Guajira)
print("La desviacion estandar en la temparatura de la Santander fue de: ",s1)
print("La desviacion estandar en la temperatura de la Narigno fue de: ",s2)
print("La desviacion estandar en la temperatura de la Guajira fue de: ",s3)
