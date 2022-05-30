import json
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
	#A list to hold the bought products
	b_product=[]
	#dict to hold checkout info
	checkout={}
	c_info={}
	#Loading products from file
	data=open_product_file()
	#Loading customers from file
	customer=open_customer_file()
	#Looping through all customers
	for c in customer["customers"]:
		#Checking for particular cusomter with matching id
		#print(c)
		if key == c["id"]:
			print(c)
			p_data=check_for_product(choice)
			print(p_data)
			c_info={"customer_id":c["id"],"product_id":p_data["id"],"customer":c["name"],"product":p_data["name"]}
			b_product.append(c_info)
			checkout={"reciepts:":b_product}
			#writng checkout information to file
			save_to_file(filename3,checkout)
			#updating product stock
			update_product1()
			#updating customers wallet
			update_customer1()
		
	

				

def open_product_file():
	with open(filename2) as file:
		data=json.load(file)
	return data

def open_customer_file():
	with open(filename1) as file:
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


def update_product1(p_id):
	data=open_product_file()
	u_product=[]
	new_products={}
	for product_data in data["products"]:
		if p_id == product_data["id"]:
			quantity=int(product_data["quantity"])
			quantity=quantity-1
			product_data["quantity"]=quantity
			print(product_data)
		u_product.append(product_data)
		new_products={"products":u_product}
	print(new_products)
	save_to_file(filename2,new_products)


def update_customer1(c_id,p_id):
	data=open_customer_file()
	p_data=check_for_product(p_id)
	u_customer=[]
	new_customers={}
	price=int(p_data["price"])
	for customer_data in data["customers"]:
		if c_id == customer_data["id"]:
			wallet=int(customer_data["wallet"])
			wallet=wallet-price
			customer_data["wallet"]=wallet
			print(customer_data)
		u_customer.append(customer_data)
		customers={"customers":u_customer}
	print(customers)
	save_to_file(filename1,customers)
	pass

purchase()
