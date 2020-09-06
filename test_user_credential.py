import unittest
# from user_credentials import user

class TestUser(unittest.TestCase):

	'''
	Test class that defines cases for the user class behaviour
	'''

	def setUp(self):
		'''
		Function to create a user account before eact test 
		'''
		self.new_user = User('Noble','Mungu','pswd100')

	def tst__init__(self):
		'''
		Test to if check the initializattion of user instance is properlly done
		'''
		self.assertEqual(self.new_user.first_name,'Noble')
		self.assertEqual(self.new_user.last_name,'Mungu')
		self.assertEqual(self.new_user.password,'pswd100')





if __name__ == '__main__':
	unittest.main()