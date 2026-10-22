class GestorGastos:
    def __init__(self, gastos):
        self.gastos = gastos

    def agregar_gasto(self, descripcion, monto, categoria):
        try:
            monto = float(monto)
        except ValueError:
            print("El monto debe ser un número. Gasto no agregado.")
            return None

        nuevo_gasto = {
            "descripcion": descripcion,
            "monto": monto,
            "categoria": categoria,
        }
        self.gastos.append(nuevo_gasto)
        return nuevo_gasto

    def ver_gastos(self):
        for gasto in self.gastos:
            print(f"{gasto['descripcion']} ({gasto['categoria']}): ${gasto['monto']}")

    def buscar_por_categoria(self, categoria_buscada):
        return [
            gasto
            for gasto in self.gastos
            if gasto["categoria"].casefold() == categoria_buscada.casefold()
        ]

    def total_por_categoria(self, categoria_buscada):
        return sum(
            gasto["monto"]
            for gasto in self.buscar_por_categoria(categoria_buscada)
        )

    def categoria_mas_costosa(self):
        totales = {}
        for gasto in self.gastos:
            categoria = gasto["categoria"]
            totales[categoria] = totales.get(categoria, 0) + gasto["monto"]
        return max(totales, key=totales.get)


def menu(gestor):
    while True:
        print("1. Ver todos los gastos")
        print("2. Agregar un gasto nuevo")
        print("3. Buscar gastos por categoria")
        print("4. Ver el total gastado en una categoria")
        print("5. Ver la categoria mas costosa")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            gestor.ver_gastos()
        elif opcion == "2":
            descripcion = input("Descripción: ")
            monto = input("Monto: ")
            categoria = input("Categoría: ")
            gestor.agregar_gasto(descripcion, monto, categoria)
        elif opcion == "3":
            categoria = input("Categoría: ")
            resultados = gestor.buscar_por_categoria(categoria)
            for gasto in resultados:
                print(f"{gasto['descripcion']} ({gasto['categoria']}): ${gasto['monto']}")
        elif opcion == "4":
            categoria = input("Categoría: ")
            total = gestor.total_por_categoria(categoria)
            print(f"Total gastado en {categoria}: ${total:.2f}")
        elif opcion == "5":
            print(f"Categoría más costosa: {gestor.categoria_mas_costosa()}")
        elif opcion == "0":
            print("Hasta luego")
            break


def main():
    gastos_negocio = [
        {"descripcion": "Renta del local", "monto": 15000.00, "categoria": "Renta"},
        {"descripcion": "Compra de insumos", "monto": 3500.00, "categoria": "Insumos"},
        {
            "descripcion": "Publicidad en redes",
            "monto": 1200.00,
            "categoria": "Marketing",
        },
    ]
    gestor = GestorGastos(gastos_negocio)
    menu(gestor)


if __name__ == "__main__":
    main()
