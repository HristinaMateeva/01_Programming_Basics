class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        first_letters_products = []
        for product in self.products:
            if product[0] == first_letter:
                first_letters_products.append(product)
        return first_letters_products

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += '\n'.join(sorted(self.products))
        return result


# Test code
catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
