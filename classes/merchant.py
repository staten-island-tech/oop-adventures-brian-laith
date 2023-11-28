class Merchant:
    def __init__(self,name,products):
        self.name = name
        self.products = products
    def sell(self,item):
        self.products.remove(item)
        print(f'You have purchased {item}')
        print(self.products)
    @staticmethod
    def greeting():
        print("Hello!")