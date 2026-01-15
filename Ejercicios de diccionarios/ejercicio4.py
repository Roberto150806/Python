meses =  {'01':'Enero','02':'Febrero','03':'Marzo','04':'Abril','05':'Mayo','06':'Junio','07':'Julio','08':'Agosto','09':'Septiembre','10':'Octubre','11':'Noviembre','12':'Diciembre'}
fecha = input("Introduzca una fecha: ")
fechapartida = fecha.split("/")


for mes in meses:
    mes = meses[fechapartida[1]]


print(fechapartida[0], "de" ,mes, "de" ,fechapartida[2])