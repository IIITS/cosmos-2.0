import random

def createOTP():
	GENSET = [1,2,3,4,5,6,7,8,9]

	otp = ""

	for i in range(6):
		try:
			g_i =random.randint(1,9)
			otp += str(GENSET[g_i])
		except IndexError:
			otp += '0'	
	return	otp