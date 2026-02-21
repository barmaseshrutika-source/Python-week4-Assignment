class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.total_price()
        return total

    def calculate_tax(self, tax_percent):
        return self.calculate_total() * tax_percent / 100

    def generate_bill(self):
        print("\n------ FINAL BILL ------")
        print("{:<15}{:<10}{:<10}{:<10}".format("Product", "Price", "Qty", "Total"))

        for product in self.products:
            print("{:<15}{:<10}{:<10}{:<10}".format(
                product.name,
                product.price,
                product.quantity,
                product.total_price()
            ))

        subtotal = self.calculate_total()
        tax = self.calculate_tax(5)  # 5% tax
        grand_total = subtotal + tax

        print("\nSubtotal:", subtotal)
        print("Tax (5%):", tax)
        print("Grand Total:", grand_total)


