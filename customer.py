class Customer:
	"""This class is for customer information"""
	customer = []
		

	# Writing customer data to .txt file
	def insert_data(self,f_name,l_name,number,email,location):
		self.customer = [f_name,l_name,number,email,location]
		files = open("customer.txt",'a')
		files.writelines(str(self.customer))
		files.close()
		pass

	#Reading customer data from .txt
	def view_data(self):
		files = open("customer.txt",'r')
		print(files.readlines())

"""customer = Customer("Ryan","Bagles","703214928","evol@haxor.com","Kenya")
customer.insert_data("Bubbles","Bubs","716737229","bubs@gmail.com","Nakuru")
customer.insert_data("Bubble","Bubs","7555555529","bubs30@gmail.com","Nairobi")
customer.view_data()"""