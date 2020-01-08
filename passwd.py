passwd = 'a123456'
passwd_count = 3

while passwd_count > 0:
	input_passwd = input('Please enter password: ')
	if input_passwd == passwd:
		print('Success')
		break
	else:
		passwd_count = passwd_count -1
		if passwd_count > 0:
			print('Error!', passwd_count, "chance")

