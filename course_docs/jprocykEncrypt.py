""" jpEncrypt.py   
	- Encrypt/Decrypt 
	- j procyk
	- 1/22/2013
	- BIA660
	
	Part 1: Uses a given password to encode and decode the message
		- No spaces allowed in password
		- Internally, password is translated to pig latin to try to thwart dictionary attacks
		- the pig latin password is used to encode the msg
		- password is recycled as necessary to encode the entire message
		- encrypted msg = (ascii code of the password[i] + ascii code of the message[j])/2.
		- If there is a remainder, add a space char before the new encoded char
		- return the entire new string
		
	 Part 2: Because of the giveaway of a space character possibly tipping off the intruder
	 		to how the encoder works, a poppy seed is added wherever a space is added.
	 	- the poppyseed (after every sequence of 'space','char') is meant to add noise 
	 		to the encoded message.  
		- the encoded msg always begins with a poppyseed (".") 
			- be kind to the user - never start the string with a space character.
	 	- Poppyseeds are from the 1st paragraph of Moby Dick, all spaces and punctuation removed.
	 	- The poppyseeds can be made more secure by adding or subtracting from their ascii values.
	 
	 Part 3: Decoding is the opposite of encoding:
	 	- remove the poppyseeds by removing the second char after each space.
	 	- double the ascii value of msg[i], remove the pig latin password, including where
	 		there were 'space' characters added.
	 
	 sample msg: "this/! 101 +.' is a quick()* []   msg{}"
	 password: "killerapp"
	 encoded msg: ". oaj ksl QrAH Qa NeI MyJM Je Cm nojH iS Fliwi he la Gm Nh FsH fId Ae Mm El ml paf wCo"
	 poppyseeds: (notice from back to front of the encoded message, the second char after a space:
	 		"Call me IshmaelSomeyear" )
	 
"""

def encode(message,password):
	
	msgAsc = []
	pwdAsc=[]
	msgEncoded=""
	
	lenMsg=len(message)
	
	# translate password to pig latin internally
	p = password[0]
	pwd = password.lstrip(p) + p + "ay"
	lenPwd=len(pwd)
	
	for words in pwd:
		for ltrs in words:
			pwdAsc.append(str(ord(ltrs)))
	#print pwdAsc		
	
	for words in message:
		for ltrs in words:
			msgAsc.append(str(ord(ltrs)))
	#print msgAsc
	
	for j in range(lenMsg):
		AscEncodedLetter = (int(msgAsc[j]) + int(pwdAsc[j % lenPwd]))/2.0
		if AscEncodedLetter - float(int(AscEncodedLetter)):
			msgEncoded += " " + chr(int(AscEncodedLetter) + 1)
		else:
			msgEncoded += chr(int(AscEncodedLetter))
		#print j, int(msgAsc[j]), int(pwdAsc[i % lenPwd]), AscEncodedLetter, chr(int(AscEncodedLetter))

	msgEncoded = AddPoppySeeds(msgEncoded)
	#print "orig msg   : ", message
	#print "encoded msg: ",msgEncodedLetter
	return msgEncoded
	
	
def decode(message,password):
	#print "encoded msg: ", message

	ascMsg = []
	pwdAsc = []
	MsgDecoded = ""
	
	# translate password to pig latin internally
	p = password[0]
	pwd = password.lstrip(p) + p + "ay"
	lenPwd = len(pwd)

	for words in pwd:
		for ltrs in words:
			pwdAsc.append(str(ord(ltrs)))
	#print pwdAsc		

	message = RemovePoppySeeds(message)
	
	SubtrFromNextVal=0
	for e in message:
		if e == " " :
			SubtrFromNextVal = 1
		else:
			ascMsg.append(ord(e)*2 - SubtrFromNextVal)
			SubtrFromNextVal = 0
	#print ascMsg

	for j in range(len(ascMsg)):
		#print j, ascMsg[j], pwdAsc[i % lenPwd] , ascMsg[j] - int(pwdAsc[i % lenPwd]), chr(ascMsg[j] - int(pwdAsc[i % lenPwd]))
		MsgDecoded += chr(ascMsg[j] - int(pwdAsc[j % lenPwd]))
	#print "decoded MsgDecoded: ", MsgDecoded
	return MsgDecoded
	
	
def AddPoppySeeds(message):
	poppyseed=MobyDick()
	countseeds=len(poppyseed)

	iseed=0
	ilen = len(message)
	msg = list(message)
	for i in range(ilen-2,-1,-1):
		if msg[i] == " ":
			msg[i+1] +=  poppyseed[iseed % countseeds]
			iseed += 1
	msg = "." + "".join(msg)
	#print msg
	return msg
		
		
def RemovePoppySeeds(message):
	message = message.replace(".","",1)
	
	ilen = len(message)
	msg = list(message)
	for i in range(ilen-2,-1,-1):
		if msg[i] == " ":
			msg.pop(i+2)
	msg = "".join(msg)
	#print msg
	return msg


def MobyDick():
	mobydick=("CallmeIshmaelSomeyearsagonevermindhowlong"
	"preciselyhavinglittleornomoneyinmypurseandnothingparticular"
	"tointerestmeonshoreIthoughtIwouldsailaboutalittleandseethewatery"
	"partoftheworldItisawayIhaveofdrivingoffthespleenandregulatingthe"
	"circulationWheneverIfindmyselfgrowinggrimaboutthemouthwheneveritis"
	"adampdrizzlyNovemberinmysoulwheneverIfindmyselfinvoluntarilypausing"
	"beforecoffinwarehousesandbringinguptherearofeveryfuneralImeetand"
	"especiallywhenevermyhyposgetsuchanupperhandofmethatitrequiresastrong"
	"moralprincipletopreventmefromdeliberatelysteppingintothestreetand"
	"methodicallyknockingpeopleshatsoffthenIaccountithightimetogettosea"
	"assoonasIcanThisismysubstituteforpistolandballWithaphilosophicalflourish"
	"CatothrowshimselfuponhisswordIquietlytaketotheshipThereisnothingsurprising"
	"inthisIftheybutknewitalmostallmenintheirdegreesometimeorothercherishvery"
	"nearlythesamefeelingstowardstheoceanwithme")
	return mobydick


if __name__ == "__main__":    
	teststring = "This is some text to be encoded"
	testpwd = "Password"
	assert(teststring != encode(teststring,testpwd))
	assert(testpwd != encode(teststring,testpwd))
	assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
	encoded = encode(teststring,testpwd)
	assert(teststring == decode(encoded,testpwd))
	print "Success!"
	
	#pwd = "~~!ab[c~!H0-9Z~Z}!!}!"
	#OrigMsg = "Hey Chester! - why c_-+an't $(123__4567890.00) ~ ~ this be a new abc~HZ~Z} 123$(-123456+(7890.00)4567890something or other ~ and then some"
#	pwd="killerapp"
#	OrigMsg = "this/! 101 +.' is a quick()* []   msg{}"
#	CodedMsg = encode(OrigMsg, pwd)
#	DecodedMsg = decode(CodedMsg, pwd)
#
#	print "Original msg: ", OrigMsg
#	print "Coded msg   : ", CodedMsg
#	print "Decoded msg : ", DecodedMsg
	
