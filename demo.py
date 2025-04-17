# class Product():
#     def __init__(self, code, nam, supplier, price):
#         info(code, nam, supplier, price)
    
# def info(code, nam, supplier, price):
#         print(f"Code : {code} Name : {nam} Supplier : {supplier} Price : {price}")

# name = input("Enter the name : ")
# supplier = input("Enter the supplier : ")
# code =  input("Enter the code : ")
# price = int(input("Enter the price : "))

# obj = Product(code, name, supplier, price)


class Product():
   
    def __init__(self, code, name, supplier, price):
        self.code = code
        self.name = name
        self.supplier = supplier
        self.price = price

    def info(self):
        print(f"Code : {self.code}\nName : {self.name}\nSupplier : {self.supplier}\nPrice : {self.price}")

class ProductManagement():
    productlist = []

    def addProduct(self,Newproduct):
        self.productlist.append(Newproduct)

    def listProduct(self):
        print("Products : ")
        for prod in self.productlist:
            prod.info()
            
    
    def searchProductBySupplier(self, supplier):
        print(f"\nSupplier {supplier}'s products :")
        for i in self.productlist:
            if i.supplier == supplier:
                print(i.name,"\t")
            else:
                continue
        
    def searchByPriceRange(self,min,max):
        for prod in self.productlist:
            if prod.price >= min and prod.price <=max :
                prod.info()
            else:
                print("No products in the range")
                break


obj = ProductManagement()

prod1 = Product(1,'Laptop', 'MSI', 46000)

obj.addProduct(prod1)


prod2 = Product(2,'Mobile', 'Motorola', 700)
prod3 = Product(3,'Washing Machine', 'Samsung', 70000)
prod4 = Product(4,'TV', 'Samsung', 460000)

obj.addProduct(prod2)
obj.addProduct(prod3)
obj.addProduct(prod4)

obj.listProduct()
obj.searchProductBySupplier('MSI')
obj.searchProductBySupplier('Samsung')

print("\nThe products from min to max price range are : ")
obj.searchByPriceRange(46,460)

print("\n")