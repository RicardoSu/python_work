class User:
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		print(f'Full name: {self.first_name} {self.last_name}')

	def greet_user(self):
		print(f'Hello {self.first_name}!')

class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = []
		
	def show_prviledges(self):
		for privilege in self.privileges:
			print(privilege)


user1 = Admin('mario','armario')
user1.privileges = ['can add a post',
	 'can delete a post',
	'can ban user']

user1.show_prviledges()




