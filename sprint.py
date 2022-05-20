import argparse
import customer as customers
import product as products

#function to insert data to file
c = customers
p = products.Product()
product_list = []
def insert_customer():
	name = input("Enter firt name :")
	name2 = input("Enter last name :")
	phone_num = input("Enter phone number :")
	email = input("Enter email :")
	location = input("Enter your location :")
	c = customers.Customer()
	c.insert_data(name,name2,phone_num,email,location)
	
#print(m.Customer.customer_id)
#insert_customer()

#Reading all customer data
def read_customer():
	c.Customer.view_data(c)

#Inserts product data
def insert_product():
	product_name = input("Enter product name :")
	quantity = input("Enter quantity :")
	p = products.Product()
	p.insert_product(product_name,quantity)
	p.view_product()

#View products
def read_product():
	p.view_product()


#modifies product data
def update_product():
	key=input("Enter product key :")
	value=input("Enter new value :")
	p.update_product(key,value)

#deletes product
def delete_product():
	key=input("Enter product key :")
	p.delete_product(key)
	

#searches for product
def search_product():
	key=input("Enter product key :")
	p.search_product(key)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Welcome to JENGA Sprint POC")
	parser.add_argument("-i,",dest="insert",action='store_const',const=True, help="insert customer data ")
	parser.add_argument("-r,",dest="display",action='store_const',const=True, help="displays customer data ")
	parser.add_argument("-p,",dest="products",action='store_const',const=True, help="inserts product data")
	parser.add_argument("-o,",dest="view",action='store_const',const=True, help="shows available  products")
	parser.add_argument("-u,",dest="update",action='store_const',const=True, help="updates product data")
	parser.add_argument("-d,",dest="deletes",action='store_const',const=True, help="deletes product data")
	parser.add_argument("-s,",dest="search",action='store_const',const=True, help="search for product")
	parsed_args = parser.parse_args()

	if parsed_args.insert:
		insert_customer()
	elif parsed_args.display:
		read_customer()
	elif parsed_args.products:
		insert_product()
	elif parsed_args.view:
		read_product()
	elif parsed_args.update:
		update_product()
	elif parsed_args.deletes:
		delete_product()
	elif parsed_args.search:
		search_product()
