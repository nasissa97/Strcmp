from pwn import *
import struct

r = remote("twinpeaks.cs.ucdavis.edu",30004)
line = r.recvline()
print(line)
line = r.recvline()
print(line)

password = ''


for x in range(20): # in assingment we are told length of the password

	char_found = False
	alpha = 'abcdefghijklmnopqrstuvwxyz' # password consist only chars
	while not char_found:
        # because we can't try every posisble characters to a limit of trials
        # I used idea of pivot pt to find the char faster
		mid = (len(alpha)) // 2
		#print(mid, " ", len(alpha), "  ",alpha)
		guess = password + alpha[mid]
	        # send guss to sever	
		r.sendline(str(guess).encode())
		
		line1 = r.recvline()
                """
                debugging purposes

		line1 = line1.decode("ASCII")
		print(line1)
		line2 = r.recvline()
		line2 = line2.decode("ASCII")
		print(line2)
                """

                # if char comes after guessed char then change alpha to the second half of list 
		if '-1' in line1:
			print('_____________--------------------')
			alpha = alpha[mid:]
	        # if char comes before guessed, return the first half of the list 
		else:
			alpha = alpha[:mid]
			print("I found 1")

                # when len is 1 found the correct char  
		if (len(alpha) == 1): 
			char_found = True

        #update password
	password = password + alpha
	print(password)


