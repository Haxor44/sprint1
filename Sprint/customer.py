from  customer1 import *
from purchase import open_customer_file,save_to_file,filename1
import random
import json




#inserting user data
def insert_data():
	m=[]
	new_customers={}
	#reading data stored in in file in order to write together with new data
	with open("customers.json") as file1:
		data=json.load(file1)
	for d in data["customers"]:
		m.append(d)
	customer_id =str(random.randint(1000, 9999))
    #getting user input
	name=input("Enter name:")
	l_name=input("Enter l_name:")
	email=input("Enter email:")
	number=input("Enter number:")
	wallet=input("Enter Amount of cash:")
    #instantitating customer object
	customer = Customer(customer_id,name,l_name,email,number,wallet)
    #storing customer object data in dictionary
	customers = {"id":customer.customer_id,"name":customer.name,"l_name":customer.l_name,"email":customer.email,"number":customer.number,"wallet":customer.wallet}
	m.append(customers)
	new_customers={"customers":m}
	with open("customers.json","w") as file:
		file.write(json.dumps(new_customers,indent=2,separators=(", ", ": "),sort_keys=True))

#display users
def display_customers():
	#reading stored data from json file
	with open("customers.json") as file :
		data = json.load(file)
		for customers in data["customers"]:
			print("**************")
			print("Customer id" "->"+customers["id"])
			print("Customer name" "->"+customers["name"])
			print("Customer last name" "->"+customers["l_name"])
			print("Customer email" "->"+customers["email"])
			print("Customer number" "->"+customers["number"])
			print("------------------")
			


#To update cusomer data by passing in id
def update_customer():
	print("1- Update customer name")
	print("2- Update customer number")
	print("3- Update customer email")
	#Taking input from user
	choice=input("Enter your choice: ")
	#taking customer id from user
	key=input("Enter id:")
	data=open_customer_file()
	new_data=[]
	new_record={}
	for customer in data["customers"]:

		if choice == "1":
			#checking for matching id
			if key == customer["id"]:	
				name=input("Enter new name: ")
				customer["name"]=name
				print("***Updated Successfully!!!***")
			new_data.append(customer)
			new_record={"customers":new_data}
			#saving to changes to file
			save_to_file(filename1,new_record)
			

		elif choice == "2":
			#checking for matching id
			if key == customer["id"]:
				number=input("Enter new number: ")
				customer["number"]=number
				print("***Updated Successfully!!!***")
			new_data.append(customer)
			#storing data in dictionary to later use in json file
			new_record={"customers":new_data}
			#saving to changes to file
			save_to_file(filename1,new_record)

		elif choice == "3":
			#checking for matching id
			if key == customer["id"]:
				email=input("Enter new email: ")
				customer["email"]=email
				print("***Updated Successfully!!!***")
			new_data.append(customer)
			new_record={"customers":new_data}
			#saving to changes to file
			save_to_file(filename1,new_record)

		elif choice == "4":
			#checking for matching id
			if key == customer["id"]:
				wallet=input("Enter new wallet amount: ")
				if int(wallet) <= 100000:
					customer["wallet"]=wallet
					print("***Updated Successfully!!!***")
			new_data.append(customer)
			new_record={"customers":new_data}
			#saving to changes to file
			save_to_file(filename1,new_record)



#to delete customer
def delete_customer():
	new_data=[]
	new_record={}
	#getting user input
	key=input("Enter customer id: ")
	#reading data from file
	data=open_customer_file()
	#looping through dictionaries
	for customer_data in data["customers"]:
		#return all other keys that do not match key entered and save them to file
		if key != customer_data["id"]:
			new_data.append(customer_data)
			new_record={"customers":new_data}
			with open("customers.json","w") as file:
				file.write(json.dumps(new_record,indent=2,separators=(", ", ": "),sort_keys=True))
		display_customers()
		print("***Deleted Successfully!!!***")

def search_customer():
	customer=input("Enter customer id to search: ")
	data=open_customer_file()
	for customers in data["customers"]:
			if customer == customers["id"]:
				print("**************")
				print("Customer id" "->"+customers["id"])
				print("Customer name" "->"+customers["name"])
				print("Customer last name" "->"+customers["l_name"])
				print("Customer email" "->"+customers["email"])
				print("Customer number" "->"+customers["number"])
				print("------------------")

def show_all_customers():
	data=open_customer_file()
	print(len(data["customers"]))

def customer():
	choice =0

	while(choice !="7"):
		print("------------------------------\n")
		print("WELCOME TO POS CUSTOMERS MENU\n")
		print("------------------------------\n")
		print("****")
		print("Total Number Of Customers:")
		show_all_customers()
		print("****\n")

		print("1- Enter Customer")
		print("2- Show Customer")
		print("3- Update Customer")
		print("4- Delete Customer")
		print("5- Search Customer")
		print("7- Exit")
		choice= input(":")
		#to insert data press1
		if choice == "1" :
			insert_data()

		#to display data enter 2
		elif choice == "2":
			display_customers()
		#to update customer data enter3
		elif choice == "3":
			update_customer()

		#to delete customer data enter 4
		elif choice == "4":
			delete_customer()

		#to search for specific customer
		elif choice == "5":
			search_customer()

		#To exit program enter 7
		elif choice == "7":
			break

		else:
			print("Wrong option")

	
