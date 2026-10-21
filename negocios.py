gastos_negocio	=	[
{"descripcion":	"Renta	del	local",	"monto":	15000.00,	"categoria":	"Renta"},
{"descripcion":	"Compra	de	insumos",	"monto":	3500.00,	"categoria":	"Insumos"},
{"descripcion":	"Publicidad	en	redes",	"monto":	1200.00,	"categoria":	
"Marketing"},
]

def	agregar_gasto(gastos,	descripcion,	monto,	categoria):
    nuevo_gasto	=	{"descripcion":	descripcion,	"monto":	monto,	"categoria":	categoria}
    gastos.append(nuevo_gasto)
    return	nuevo_gasto
def	ver_gastos(gastos):
    for	gasto	in	gastos:
        print(f"{gasto['descripcion']}	({gasto['categoria']}):	${gasto['monto']}")

def buscar_por_categoria(gastos, categoria_buscada):
    return [
        gasto
        for gasto in gastos
        if gasto["categoria"].casefold() == categoria_buscada.casefold()
    ]

def total_por_categoria(gastos, categoria_buscada):
    return sum(
        gasto["monto"]
        for gasto in buscar_por_categoria(gastos, categoria_buscada)

    )


print(buscar_por_categoria(gastos_negocio,	"INSUMOS"))
print(total_por_categoria(gastos_negocio,	"insumos"))

while True:
    print("1. Ver todos los gastos")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        ver_gastos(gastos_negocio)
    elif opcion == "0":
        print("Hasta luego")
        break