#enable the password to be hidden from the prompt
import getpass

#ask for a for response 
while True: 
	answer = input('Have you been here before? y|n \n')
	if answer == 'y':
		been_here = True
		break
	elif answer == 'n':
		been_here = False
		break
	else:
		print('enter y or n')

#validate the password and username
if been_here:
	with open(r'C:\Users\Simba\Desktop\python_works\userinfo.txt','r') as f:
		username = f.readline().rstrip('\n')
		password = f.readline().rstrip('\n')
		if input('Enter username:') != username:
			print('wrong username')
		elif input('Password: ') != password:
			print('Wrong password') 
		else:
			print('Correct credentials')
			
#if there is nothing in the file, then ask the user to input
#password and username			
else:
	username = input('Enter your username: ')
	password = getpass.getpass('Enter your password: ')
	with open(r'C:\Users\Simba\Desktop\python_works\userinfo.txt','w') as f:
		print(username , file = f)
		print(password , file = f)
	print('Done, run the file again')
	
