import pyperclip
from user_credentials import User , Credential

def create_user(fname,lname,password):
    '''
    Function to create a new user account
    '''
    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user account
    '''
    User.save_user(user)


def verify_user(first_name,password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    checking_user = Credential.check_user(first_name,password)
    return checking_user

def generate_password():
    '''
    Function to generate a password automatically
    '''
    gen_pass = Credential.generate_password()
    return gen_pass

def create_credential(user_name,site_name,account_name,password):
    '''
    Function to create a new credential
    '''
    new_credential=Credential(user_name,site_name,account_name,password)
    return new_credential

def save_credential(credential):
    '''
    Function to save a newly created credential
    '''
    Credential.save_credentials(credential)

def display_credentials(user_name):
    '''
    Function to display credentials saved by a user
    '''
    return Credential.display_credentials(user_name)
    
def copy_credential(site_name):
    '''
    Function to copy a credentials details to the clipboard
    '''
    return Credential.copy_credential(site_name)

def main():
	print('')
	print('Hello!Welcome to Password locker.')
	while True:
		print(' ')
		print('-'*60)
		print('Use these codes to navigate:\n ca-Create an account \n lg-login \n ex-Exit')
		short_code = input('Enter a choice:').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("-"*60)
			print(' ')
			print('To create a new account:')
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for : {first_name}{last_name} using password:{password}')
			

















if __name__ == '__main__':
	main()

