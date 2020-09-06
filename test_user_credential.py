import unittest
from user_credentials import user

class TestUser(unittest.TestCase):

	'''
	Test class that defines cases for the user class behaviour
	'''

	def setUp(self):
		'''
		Function to create a user account before eact test 
		'''
		self.new_user = User('Noble','Mungu','pswd100')

	def test__init__(self):
		'''
		Test to if check the initializattion of user instance is properlly done
		'''
		self.assertEqual(self.new_user.first_name,'Noble')
		self.assertEqual(self.new_user.last_name,'Mungu')
		self.assertEqual(self.new_user.password,'pswd100')


	def test_save_user(self):
		'''
		test to check if the new users info saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.user_list),1)
class TestCredential(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.
	Args:
		unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_usr = User('Noble','mungu','pswd100')
		self.new_user.save_user()
		user2 = User('Noble','Mungu','pswd100')
		user2.save_user()

		for user in User.user_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEquaal(current_user,Credential.check_user(user2.password,user2.first_name))

	def setUp(self):
		'''
		Function to create an account's credentials before each test
		'''
		self.new_credential = Credential('Noble','Facebook','Mungu','pswd100')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		self.assertEqual(self.new_credential.user_name,'Noble')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'Noblemungu')
		self.assertEqual(self.new_credential.password,'pswd100')

	def test_save_credentials(self):
		'''
		Test to check if the new credential info is saved into the credentials list
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Noble','Twitter','Mungu','pswd100')
		twitter.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)





if __name__ == '__main__':
	unittest.main()