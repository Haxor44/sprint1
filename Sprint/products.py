from  product import *
from purchase import open_product_file,save_to_file,check_for_product,filename2
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
	#validation
	while True:
		try:
			quantity=int(input("Enter quantity:"))
			price=int(input("Enter price:"))
		except ValueError:
			print("Please input an integer!!!")
			continue
		else:
			break
	product = Product(product_id,name,quantity,price)
    #storing product object in dictionary
	new_product = {"id":product.product_id,"name":product.name,"quantity":str(product.quantity),"price":str(product.price)}
	m.append(new_product)
	#print(m)
	new_products={"products":m}
	with open("products.json","w") as file:
		file.write(json.dumps(new_products,indent=2,separators=(", ", ": "),sort_keys=True))
	print("***Product inserted Successfully!!!***")

#display users
def display_products():
	#reading stored data from json file
	data=open_product_file()
	for products in data["products"]:
		print("**************")
		print("Product id" "->"+products["id"])
		print("Product name" "->"+products["name"])
		print("Product quantity" "->"+products["quantity"])
		print("Product price" "->"+products["price"])
		print("------------------")


#To update product data by passing in id
def update_product():
	#Taking user input from the user
	print("1- Update product name")
	print("2- Update product price")
	print("3- Update product quantity")
	choice=input("Enter your choice: ")
	#Taking product id from the user
	key=input("Enter id:")
	data=open_product_file()
	new_data=[]
	new_record={}
	for product_data in data["products"]:

		if choice == "1":
			#looking for matching id
			if key == product_data["id"]:
				name=input("Enter new name: ")
				#updating the name
				product_data["name"]=name
				print("***Updated Successfully!!!***")
			new_data.append(product_data)
			#storing data in dictionary to later use in json file
			new_record={"products":new_data}
			#saving to changes to file
			save_to_file(filename2,new_record)
				

		elif choice == "2":
			#looking for matching id
			if key == product_data["id"]:
				while True:
					try:
						price=int(input("Enter new price:"))
					except ValueError:
						print("Please enter int!!!")
						continue
					else:
						break
				#updating the price
				product_data["price"]=str(price)
				print("***Updated Successfully!!!***")
			new_data.append(product_data)
			new_record={"products":new_data}
			save_to_file(filename2,new_record)

		elif choice == "3":
			if key == product_data["id"]:
				while True:
					try:
						quantity=int(input("Enter new amount: "))
					except ValueError:
						print("Please enter int!!!")
						continue
					else:
						break
				product_data["quantity"]=str(quantity)
				print("***Updated Successfully!!!***")
			new_data.append(product_data)
			#storing data in dictionary to later use in json file
			new_record={"products":new_data}
			#saving to changes to file
			save_to_file(filename2,new_record)
		
	
	

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

def search_product():
	product=input("Enter product id to search: ")
	with open("products.json") as file :
		data = json.load(file)
	for products in data["products"]:
		if product == products["id"]:
			print("**************")
			print("Product id" "->"+products["id"])
			print("Product name" "->"+products["name"])
			print("Product quantity" "->"+products["quantity"])
			print("Product price" "->"+products["price"])
			print("------------------")
	print("Search Completed!!!")




def show_all_products():
	data=open_product_file()
	print(len(data["products"]))

def product():
	choice =0

	while(choice !="7"):

		print("------------------------------\n")
		print("  WELCOME TO POS PRODUCTS MENU \n  ")
		print("------------------------------\n")
		print("****")
		print("Total Number Of Products:")
		show_all_products()
		print("****\n")

		print("1 - Enter Product")
		print("2 - Show Products")
		print("3 - Update Products")
		print("4 - Delete Products")
		print("5 - Search Products")
		print("6 - **Go To Customer Menu**")
		print("7 - **Go To Purchase Menu** ")
		print("8 - Exit\n")
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

		#to search for a product
		elif choice == "5":
			search_product()

		elif choice == "6":
			from customer import customer
			customer()

		elif choice == "7":
			from purchase import purchase_menu
			purchase_menu()

		#To exit program enter 7
		elif choice == "8":
			break

		else:
			print("Wrong option")

	



	

