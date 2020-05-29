import zmail, sys
from datetime import datetime
from colorama import init, Fore, Back, Style

# Details of the Email Account You want to send the Emails from:
	
Username = '' # Insert Your Email Username Here
Password = '' # Insert Your Email Password Here

# Script:
	
Quantity = input ('Quantity of Tasks: ')
Quantity = int(Quantity)
print('-------------')
count = 0
while (count < Quantity):

	count = count + 1
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	Subject = 'Email Successfully Received - '+str(count)
	
	try:
		f=open('Emails.txt')
		line=f.readlines()
		Email = line[count]
	except IndexError:
		print('')
		print('['+current_time+']'+ Fore.YELLOW + ' All Emails Tested!')
		sys.exit()

	mail = {
		'from':'Forwarding Success! <mymail@foo.com>',
		'subject': Subject,
		'content_text': 'This was a test to ensure your emails are forwarding correctly. Made By Aj#0069', 
	}
		
	try:
		server = zmail.server(Username, Password)
		server.send_mail(Email, mail)
		print('['+current_time+']'+ Fore.GREEN + ' Successfully Sent Email to: '+ Fore.WHITE +Email)

	except:
		print('['+current_time+']'+ Fore.YELLOW + ' Unable To Send Email - '+Email)
