class Chair:

    def __init__(self, name):
        self.name = name

    def sit(self):
        pass


class Sofa:

    def __init__(self, name):
        self.name = name

    def sit(self):
        pass


class WoodenChair(Chair):

    def sit(self):
        print(f"Деревянный стул ({self.name})")


class WoodenSofa(Sofa):

    def sit(self):
        print(f"Деревянный диван ({self.name})")


class PlasticChair(Chair):

    def sit(self):
        print(f"Пластиковый стул ({self.name})")


class PlasticSofa(Sofa):

    def sit(self):
        print(f"Пластиковый диван ({self.name})")


class FurnitureFactory:

    def create_chair(self):
        pass

    def create_sofa(self):
        pass


class WoodenFurnitureFactory(FurnitureFactory):

    def create_chair(self, name):
        return WoodenChair(name)

    def create_sofa(self, name):
        return WoodenSofa(name)


class PlasticFurnitureFactory(FurnitureFactory):

    def create_chair(self, name):
        return PlasticChair(name)

    def create_sofa(self, name):
        return PlasticSofa(name)


wooden_factory = WoodenFurnitureFactory()
wooden_chair = wooden_factory.create_chair("Стул ОАК")
wooden_sofa = wooden_factory.create_sofa("Диван деревянный / скамья")
wooden_chair.sit()
wooden_sofa.sit()

plastic_factory = PlasticFurnitureFactory()
plastic_chair = plastic_factory.create_chair("Мебельторг Алания Белый")
plastic_sofa = plastic_factory.create_sofa("Диван пластиковый ReeHouse Net Белый")
plastic_chair.sit()
plastic_sofa.sit()