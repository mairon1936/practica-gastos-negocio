from negocios import GestorGastos, gastos_negocio


def main():
    gestor = GestorGastos(gastos_negocio)
    print("Gastos del negocio:")
    gestor.ver_gastos()


if __name__ == "__main__":
    main()
