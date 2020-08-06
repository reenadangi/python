class Store:
    def __init__(self,name):
        self.name=name
        self.lst_products=[]
    def add_product(self,new_product):
        self.lst_products.append(new_product)
        return self
    def show_products(self):
        print("*"*20,"\nWelcome to"+self.name,"\n","*"*20)
        for prod in self.lst_products:
            prod.print_info()
    # sell_product(self, id) 
    def sell_product(self, id):
        self.lst_products.pop(id)
    # inflation(self, percent_increase)
    def inflation(self, percent_increase):
        self.lst_products
        for prod in self.lst_products:
            prod.update_price(percent_increase,True)
    # set_clearance(self, category, percent_discount)
    def set_clearance(self, category, percent_discount):
        for prod in self.lst_products:
            if(prod.category==category):
                prod.update_price(percent_discount,False)

class Product:
    
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category

    def update_price(self, percent_change, is_increased) :
        if(is_increased):
            self.price=self.price+(percent_change/100)
        else:
            self.price=self.price-(percent_change/100)
        return self
    def print_info(self):
        print(self.name, self.category, self.price)
    def show_details(self):
        print(self.name,self.category,self.price)


prod1=Product("phone",2000,"Tech")
prod2=Product("TV",2000,"Tech")
prod3=Product("Airpods",1000,"Tech")
# prod1.show_details()

store=Store("BestBUY")

store.add_product(prod1)
store.add_product(prod2)
store.add_product(prod3)
store.show_products()
store.sell_product(2)
store.show_products()
store.inflation(2)
store.show_products()
store.set_clearance("Tech",10)
store.show_products()

# Store.show_products()