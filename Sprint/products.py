from  product import *
import random
import json

def insert_product():
	m=[]
	new_products={}
	#reading data stored in in file in order to write together with new data
	with open("products.json") as file1:
		data=json.load(file1)
	for d in data["products"]:
		m.append(d)
	product_id =str(random.randint(1000, 9999))
    #getting user input
	name=input("Enter name:")
	quantity=input("Enter quantity:")
    #instantitating product object
	product = Product(product_id,name,quantity,price)
    #storing product object in dictionary
	new_product = {"id":product.product_id,"name":product.name,"quantity":product.quantity,"price":product.price}
	m.append(new_product)
	#print(m)
	new_products={"products":m}
	with open("products.json","w") as file:
		file.write(json.dumps(new_products,indent=2,separators=(", ", ": "),sort_keys=True))
	print("***Product inserted Successfully!!!***")

#display users
def display_products():
	#reading stored data from json file
	with open("products.json") as file :
		data = json.load(file)
		for products in data["products"]:
			print("**************")
			print("Product id" "->"+products["id"])
			print("Product name" "->"+products["name"])
			print("Product quantity" "->"+products["quantity"])
			print("Product price" "->"+products["price"])
			print("------------------")

#To update product data by passing in id
def update_product():
	#Taking user input
	key=input("Enter customer id: ")
	name=input("Enter new name: ")
	quantity=input("Enter new  amount: ")
	price=input("Enter new  price: ")
	new_data=[]
	new_record={}
	#Reading stored data from json file
	with open("products.json") as file :
		data = json.load(file)
	#looping through dictionaries and searching for entered key
	for product_data in data["products"]:
		if key == product_data["id"]:
			#applying new changes
			product_data["id"]=key
			product_data["name"]=name
			product_data["quantity"]=quantity
			product_data["price"]=price
		new_data.append(product_data)
		new_record={"products":new_data}
		#writing new data together with previous data to file
		with open("products.json","w") as file:
			file.write(json.dumps(new_record,indent=2,separators=(", ", ": "),sort_keys=True))
		display_products()
		print("***Updated Successfully!!!***")
		
	
	

#to delete product by entering id
def delete_product():
	new_data=[]
	new_record={}
	#getting user input
	key=input("Enter product id: ")
	#reading data from file
	with open("products.json") as file :
		data = json.load(file)
	#looping through dictionaries
	for product in data["products"]:
		#return all other keys that do not match key entered and save them to file
		if key != product["id"]:
			new_data.append(product)
			new_record={"products":new_data}
			with open("products.json","w") as file:
				file.write(json.dumps(new_record,indent=2,separators=(", ", ": "),sort_keys=True))
		display_products()
		print("***Deleted Successfully!!!***")



def main():

	choice =0

	while(choice !="7"):

		print("1- Enter Product")
		print("2- Show Product")
		print("3- Update Product")
		print("4- Delete Product")
		print("7- Exit\n")
		choice= input(":")
		#to insert data press1
		if choice == "1" :
			insert_product()

		#to display data enter 2
		elif choice == "2":
			display_products()
		#to update customer data enter3
		elif choice == "3":
			update_product()

		#to delete customer data enter 4
		elif choice == "4":
			delete_product()

		#To exit program enter 7
		elif choice == "7":
			break

		else:
			print("Wrong option")

	
if __name__ == "__main__":
	main()


	

