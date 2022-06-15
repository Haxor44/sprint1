import json
import random
import datetime


filename1="customers.json"
filename2="products.json"
filename3="reciepts.json"

def purchase():
	#Showing the available products
	available_products()
	#Entering the user to make the purchase
	key=input("Enter customer id: ")
	#product to be bought

	#a list to hold receits if any
	reciepts=[]
	sell=True
	reciept_id =str(random.randint(1000, 9999))
	data2=open_reciepts_file()
	for d in data2["reciepts"]:
		reciepts.append(d)
	#dict to hold checkout info
	checkout={}
	c_info={}
	ls=[]
	#Loading products from file
	data=open_product_file()
	#Loading customers from file
	customer=open_customer_file()
	while sell:
		exit=input("Enter 1 - to keep selling and 2 - print receipt:")
		if exit !="2":
			choice=input("Enter product id: ")
			amount=input("Enter product amount: ")
		#Looping through all customers
			for c in customer["customers"]:
			#Checking for particular cusomter with matching id
			#print(c)
				if key == c["id"]:
					date=datetime.date.today()
					check_amount(amount)
					p_data=check_for_product(choice)
					total=int(amount)*int(p_data["price"])
					c_info={"reciept_id":reciept_id,"customer_id":c["id"],"product_id":p_data["id"],"customer":c["name"],"product":p_data["name"],"Total Amount:":str(total),  "Quantity":str(amount),"price":p_data["price"],"Date":str(date)}
					ls.append(c_info)
			reciepts.append(c_info)
			checkout={"reciepts":reciepts}


		elif exit == "2":
			sell=False
			#writng checkout information to file
			save_to_file(filename3,checkout)
			for i in ls:
				#updating product stock
				update_product1(i["product_id"],i["Quantity"])
				#updating customers wallet
				update_customer1(key,i["customer_id"],i["Quantity"],i["price"])

			
				

				
			print("Your reciept is: ")
			print("**************")
			print("Receipt id: " "->"+reciept_id)
			print("Customer id" "->"+c["id"])
			print("Customer name" "->"+c["name"])
			print("Products bought" "->"+str(ls))
			print("Total amount" "->"+str(total))
			print("Date" "->"+str(date))
			print("Thanks for shopping with us!!!!")
			print("(:")
			print("**************")
			purchase_menu()
		
		else:
			print("Wrong option Entered")

				
def available_products():
	data=open_product_file()
	for products in data["products"]:
		print("**************")
		print("Product id" "->"+products["id"])
		print("Product name" "->"+products["name"])
		print("Product quantity" "->"+products["quantity"])
		print("Product price" "->"+products["price"])
		print("------------------")

def check_amount(amount):
	data=open_product_file()
	for product in data["products"]:
		if amount < product["quantity"]:
			return amount

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



def update_customer1(c_id,p_id,amount,price):
	data=open_customer_file()
	amount=int(amount)
	price1=int(price)*amount
	u_customer=[]
	new_customers={}
	for customer_data in data["customers"]:
		if c_id == customer_data["id"]:
			wallet=int(customer_data["wallet"])
			if wallet>price1:
				wallet=wallet-price1
				customer_data["wallet"]=str(wallet)
			else:
				print("Not enough money!!!")
		u_customer.append(customer_data)
		customers={"customers":u_customer}
	save_to_file(filename1,customers)
	
def all_transactions():
	with open(filename3) as file:
		data=json.load(file)
		for purchase in data["reciepts"]:
			print("**************")
			print("purchase id" "->"+purchase["reciept_id"])
			print("purchased product name" "->"+purchase["product"])
			print("purchasing customer name" "->"+purchase["customer"])
			print("purchase quantity" "->"+purchase["Quantity"])
			print("purchase date" "->"+purchase["Date"])
			#print("purchase price" "->"+purchase["price"])
			#print("Total Amount" "->"+purchase["Total Amount"])
			print("------------------")
def purchase_menu():
	choice=0
	while(choice !="7"):
		print("------------------------------\n")
		print("WELCOME TO POS PURCHASE MENU")
		print("------------------------------\n")
		print("1 - Sell Product")
		print("2 - View All Transactions")
		print("7- Exit\n")
		choice= input(":")
		#to insert data press1
		if choice == "1":
			purchase()

		elif choice == "2":
			all_transactions()
		#To exit program enter 7
		elif choice == "7":
			break
		else:
			print("Wrong option")

