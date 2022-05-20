class Product:
	"""This class contains product data"""
	products = {}
	
	#Insert product data to .txt
	def insert_product(self,name,amount):
		self.products[name] = amount
		files1 = open("products.txt",'a')
		files1.writelines(str(list(self.products.items())))
		files1.close()
		pass

	#view product data
	def view_product(self):
		#print(list(self.products.items()))
		files = open("products.txt",'r')
		print(files.readlines())

	#This function searches for a product
	def search_product(self,key):
		print(self.products.get(key,"Not found"))

	
	#updates product data
	def update_product(self,key,value):
		self.products[key] = value
		files2 = open("products.txt",'w')
		files2.writelines(str(list(self.products.items())))
		files2.close()

	#This function deletes product	
	def delete_product(self,key):
		del self.products[key]
		files3 = open("products.txt",'w')
		files3.writelines(str(list(self.products.items())))
		files3.close()

"""
product = Product("Vaseline", "30")
product.insert_product("Soda","juices")
product.insert_product("juice","70")
product.insert_product("water","100")
product.insert_product("bread","90")
product.search_product("Bagles")
product.update_product("Vaseline","50")
product.delete_product("Vaseline")
product.view_product()"""


