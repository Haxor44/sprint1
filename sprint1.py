class Eagle:
	species = "Eagle"

	def __init__(self,name,age):
		self.name = name
		self.age = age

blue = Eagle("Ryan",24)
red = Eagle("Jimmy",42)

print("{} is a {}".format(blue.name,blue.__class__.species))
print("{} is also a {}".format(red.name,red.__class__.species))	