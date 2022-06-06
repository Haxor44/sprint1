import json
import random
from products import *

filename1="customers.json"
filename2="products.json"
filename3="reciepts.json"

def purchase():
	#Showing the available products
	display_products()
	#Entering the user to make the purchase
	key=input("Enter your id: ")
	#product to be bought
	choice=input("Enter product id: ")
	amount=input("Enter product amount: ")
	#a list to hold receits if any
	reciepts=[]
	reciept_id =str(random.randint(1000, 9999))
	data2=open_reciepts_file()
	for d in data2["reciepts"]:
		reciepts.append(d)
	#dict to hold checkout info
	checkout={}
	c_info={}
	#Loading products from file
	data=open_product_file()
	#Loading customers from file
	customer=open_customer_file()
	#opening the reciepts file

	#Looping through all customers
	for c in customer["customers"]:
		#Checking for particular cusomter with matching id
		#print(c)
		if key == c["id"]:
			print(c)
			p_data=check_for_product(choice)
			c_info={"reciept_id":reciept_id,"customer_id":c["id"],"product_id":p_data["id"],"customer":c["name"],"product":p_data["name"]}
			reciepts.append(c_info)
			checkout={"reciepts":reciepts}
			#writng checkout information to file
			save_to_file(filename3,checkout)
			#updating product stock
			update_product1(choice,amount)
			#updating customers wallet
			update_customer1(key,choice,int(amount))
			print("Your reciept is: ")
			print("**************")
			print("Customer id" "->"+c["id"])
			print("Customer name" "->"+c["name"])
			print("Product bought" "->"+p_data["name"])
			print("Thanks for shopping with us!!!!")
			print("**************")
		
	

				

def open_product_file():
	with open(filename2) as file:
		data=json.load(file)
	return data

def open_customer_file():
	with open(filename1) as file:
		data=json.load(file)
	return data

def open_reciepts_file():
	with open(filename3) as file:
		data=json.load(file)
	return data

def save_to_file(filename,d_dict):
	with open(filename,"w") as file:
		file.write(json.dumps(d_dict,indent=2,separators=(", ", ": "),sort_keys=True))


def check_for_product(p_key):
	data=open_product_file()
	for p_data in data["products"]:
		if p_key == p_data["id"]:
			return p_data


def update_product1(p_id,amount):
	data=open_product_file()
	u_product=[]
	new_products={}
	for product_data in data["products"]:
		if p_id == product_data["id"]:
			quantity=int(product_data["quantity"])
			amount=int(amount)
			quantity=quantity-amount
			product_data["quantity"]=str(quantity)
		u_product.append(product_data)
		new_products={"products":u_product}
	save_to_file(filename2,new_products)


def update_customer1(c_id,p_id,amount):
	data=open_customer_file()
	p_data=check_for_product(p_id)
	u_customer=[]
	new_customers={}
	price=int(p_data["price"])*amount
	for customer_data in data["customers"]:
		if c_id == customer_data["id"]:
			wallet=int(customer_data["wallet"])
			wallet=wallet-price
			customer_data["wallet"]=str(wallet)
		u_customer.append(customer_data)
		customers={"customers":u_customer}
	save_to_file(filename1,customers)

	
def purchase_menu():
	choice=0
	while(choice !="7"):
		print("------------------------------\n")
		print("WELCOME TO POS PURCHASE MENU")
		print("------------------------------\n")
		print("1- Buy product")
		print("7- Exit\n")
		choice= input(":")
		#to insert data press1
		if choice == "1":
			purchase()
		#To exit program enter 7
		elif choice == "7":
			break
		else:
			print("Wrong option")

