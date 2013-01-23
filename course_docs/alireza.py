def encode(user,password):

	encoded=user+password
	return encoded

 def decode(encoded,password):
	x=len(password)
	y=len(encoded)
	z=y-x
	user=encoded [:z]
	return user

