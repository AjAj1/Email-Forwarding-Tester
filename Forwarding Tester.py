import zmail, sys
from datetime import datetime
from colorama import init, Fore, Back, Style

# Details of the Email Account You want to send the Emails from:
	
Username = '' # Insert Your Email Username Here
Password = '' # Insert Your Email Password Here

# Script:
	
def Test():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	
	try:
		f=open('Emails.txt')
		line=f.readlines()
		Email = line[0]
	except IndexError:
		print('')
		print('['+current_time+']'+ Fore.YELLOW + ' All Emails Tested!')
		sys.exit()

	mail = {
		'from':'Forwarding Success! <mymail@foo.com>',
		'subject': 'Email Successfully Received.',
		'content_text': 'This was a test to ensure your emails are forwarding correctly. Made By Aj#0069', 
	}
	
	try:
		server = zmail.server(Username, Password)
		server.send_mail(Email, mail)

	except:
		print('['+current_time+']'+ Fore.YELLOW + ' Unable To Send Email!')
	
	print('['+current_time+']'+ Fore.GREEN + ' Successfully Sent Email to: '+ Fore.WHITE +Email)
	
	with open("Emails.txt", "w") as outfile:
		for pos, line in enumerate(line):
			if pos != 0:
				outfile.write(line)

Quantity = input ('Quantity of Tasks: ')
Quantity = int(Quantity)
print('-------------')
count = 0
while (count < Quantity):
	count = count + 1
	Test()
