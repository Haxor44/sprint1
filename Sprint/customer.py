from  customer1 import *
import random
import json

customers1={}


#inserting user data
def insert_data():
	customers={}
	cusomers1=[]
	new_customers={}
	#generating random number for id
	customer_id =str(random.randint(1000, 9999))
	#getting user input
	name=input("Enter name:")
	l_name=input("Enter l_name:")
	email=input("Enter email:")
	number=input("Enter number:")
	#instantitating customer object
	customer = Customer(customer_id,name,l_name,email,number)
	#storing customer object in dictionary
	customers = {"id":customer.customer_id,"name":customer.name,"l_name":customer.l_name,"email":customer.email,"number":customer.number}
	customers1.append(customers)
	#passing the dictionary to json
	with open("customers.json","a") as file:
		file.write(json.dumps(customers,indent=2,separators=(", ", ": "),sort_keys=True))

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
	#Taking user input
	key=input("Enter customer id: ")
	name=input("Enter new name: ")
	la_name=input("Enter new  last name: ")
	email=input("Enter new email: ")
	number=input("Enter new number: ")
	new_data=[]
	new_record={}
	#Reading stored data from json file
	with open("customers.json") as file :
		data = json.load(file)
	#looping through dictionaries and searching for entered key
	for customer_data in data["customers"]:
		if key == customer_data["id"]:
			customer_data["id"]=key
			customer_data["name"]=name
			customer_data["l_name"]=la_name
			customer_data["email"]=email
			customer_data["number"]=number
		new_data.append(customer_data)
		new_record={"customers":new_data}
		#writing new data together with previous data to file
		with open("customers.json","w") as file:
			file.write(json.dumps(new_record,indent=2,separators=(", ", ": "),sort_keys=True))
		display_customers()
		print("***Updated Successfully!!!***")
		
	
	

#to delete customer
def delete_customer():
	new_data=[]
	new_record={}
	#getting user input
	key=input("Enter customer id: ")
	#reading data from file
	with open("customers.json") as file :
		data = json.load(file)
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



def main():

	choice =0

	while(choice !="7"):

		print("1- Enter Customer")
		print("2- Show Customer")
		print("3- Update Customer")
		print("4- Delete Customer")
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

		#To exit program enter 7
		elif choice == "7":
			break

		else:
			print("Wrong option")

	
if __name__ == "__main__":
	main()

