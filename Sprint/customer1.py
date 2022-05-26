class Customer:
	"""This class is for customer information"""
	customer = {}
		

	def __init__(self,customer_id,name,l_name,email,number):
		self.customer_id=customer_id
		self.name=name
		self.l_name=l_name
		self.email=email
		self.number=number

		