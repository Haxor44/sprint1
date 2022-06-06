import argparse
from products import *
from customer import *
from purchase import *


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Welcome to JENGA Sprint POC")
	parser.add_argument("-c,",dest="customer",action='store_const',const=True, help="Go To Customer Menu ")
	parser.add_argument("-p,",dest="products",action='store_const',const=True, help="Go Product Menu")
	parser.add_argument("-P,",dest="purchase",action='store_const',const=True, help="Make Purchase")
	parsed_args = parser.parse_args()

	if parsed_args.customer:
		customer()

	elif parsed_args.products:
		product()

	elif parsed_args.purchase:
		purchase_menu()
	