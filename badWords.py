#imagine this list is the database for bad words
badWords = ['spic','sex']

#user sending a message
message = input("Your message :")

#this variable will be sent to other user
encrypt = ''

#looping for every single word in the message
for i in message.split():
	#checking if the word contain the bad word
	if i in badWords:
		#if it's contain then check if the word length is greater than the bad word length, if it's then there's should be letter after the bad word so it doesn't have to be cencored
		if len(i) > len(badWords[badWords.index(i)]):
			encrypt += i+" "
		# if it's the same length then it's the bad word so it has to be cencored
		elif len(i) == len(badWords[badWords.index(i)]):
			encrypt += i.replace(i, '*'*len(i))+" "
	# if it's not contain any bad word then don't cencored it
	else:
		encrypt += i+" "
	#send to the other user
print(encrypt)