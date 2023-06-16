class Furniture:

    def __init__(self, name):
        self.name = name

    def sit(self):
        pass


class Chair(Furniture):

    def sit(self):
        print(f"Стул ({self.name})")


class Sofa(Furniture):

    def sit(self):
        print(f"Диван ({self.name})")


class FurnitureFactory:

    def create_furniture(self, name):
        pass


class WoodenFurnitureFactory(FurnitureFactory):

    def create_furniture(self, name):
        return Chair(name)


class PlasticFurnitureFactory(FurnitureFactory):

    def create_furniture(self, name):
        return Sofa(name)


wooden_factory = WoodenFurnitureFactory()

wooden_chair = wooden_factory.create_furniture("Деревянные и пластиковые")

wooden_chair.sit()

plastic_factory = PlasticFurnitureFactory()

plastic_sofa = plastic_factory.create_furniture("Деревянные и пластиковые")

plastic_sofa.sit()