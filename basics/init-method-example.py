#!/Users/xuansong/.bin/py38
class Dog1:
    # class attribute
	attr1 = "mammal"
    # Instance attribute
	def __init__(self, name, type):
		self.name = name
		self.type=type
  
# Driver code
# Object instantiation
Rodger = Dog1("Rodger", None)
Tommy = Dog1("Tommy", None)
  
# Accessing class attributes
# What is __class__ variable?
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
  
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))



class Dog2:
    
	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.name = name
		
	def speak(self):
		print("My name is {}".format(self.name))

# Driver code
# Object instantiation
Rodger = Dog2("Rodger")
Tommy = Dog2("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()

