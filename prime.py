def prime(num):
	if num > 1:
		for i in range(2,num):
			if(num % i == 0):
				print i, "is not a prime number."
			else:
				print i, "is a prime number."

prime(5)
