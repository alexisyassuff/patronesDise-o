# Creador (interfaz)
class Pizzeria():
    def crear_pizza(self):
        pass

# Creadores concretos


class PizzeriaNapolitana(Pizzeria):
    def crear_pizza(self):
        return PizzaNapolitana()


class PizzeriaFugazzeta(Pizzeria):
    def crear_pizza(self):
        return PizzaFugazzeta()


class PizzeriaPepperoni(Pizzeria):
    def crear_pizza(self):
        return PizzaPepperoni()

# Producto base


class Pizza():
    def preparar(self):
        pass

# Productos concretos


class PizzaNapolitana(Pizza):
    def preparar(self):
        print("Preparando pizza napolitana: tomate, mozzarella, albahaca.")


class PizzaFugazzeta(Pizza):
    def preparar(self):
        print("Preparando pizza fugazzeta: cebolla, mozzarella.")


class PizzaPepperoni(Pizza):
    def preparar(self):
        print("Preparando pizza pepperoni: mozzarella, pepperoni.")

# Cliente


def main():
    print("\n --------------Pedido 1:")
    pizzeria = PizzeriaNapolitana()
    pizza = pizzeria.crear_pizza()
    pizza.preparar()

    print("\n --------------Pedido 2:")
    pizzeria = PizzeriaFugazzeta()
    pizza = pizzeria.crear_pizza()
    pizza.preparar()

    print("\n -------------- Pedido 3:")
    pizzeria = PizzeriaPepperoni()
    pizza = pizzeria.crear_pizza()
    pizza.preparar()


if __name__ == "__main__":
    main()
