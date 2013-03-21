import twitter
import string

api = twitter.Api(consumer_secret='xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI',consumer_key='HrI9pkJWwsdTL1jv9fDmg',access_token_key='19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA',access_token_secret='bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A')

''' this is a hash function which is used to compute which file the id should
    go to'''
def hashfction(user_id):
    n=0 #store the number of digits in user_id
    temp=user_id
    ''' get the number of digits in user_id '''
    while temp > 0:
        n +=1
        temp= temp/10
    hashfile=0  
    if n < 6:
        return 0   #use one hash file to store ids which is less then 6 digits
    elif n==6:
        hashfile=user_id/(10**5)  #1~9
        return hashfile  #use nine hash files to store ids which is 6 digits
    elif n==7:
        hashfile=(user_id/(10**5)-10)/2+10  #10~54
        return hashfile  #use 45 hash files to store ids which is 7 digits
    elif n==8:
        hashfile=(user_id/(10**6)-10)/2+55   #55~99
        return hashfile  #use 45 hash files to store ids which is 8 digits
    elif n==9:
        hashfile=(user_id/(10**7)-10)/2+100   #100~144
        return hashfile  #use 45 hash files to store ids which is 9 digits
    else:
        if user_id < 1300000000:
            hashfile=(user_id-1000000000)/(10**7)+145   #145~174
            return hashfile #use 30 hash files to store ids which is 10 digits and less than 1300000000
        else:
            return 175  #use one hash file to store ids which is more than 1300000000



#store the total ids    
f=open('D:\python_midterm\user_id\userid.txt','w')
count=0
#friends=api.GetFriends(379514775)635986661
friends=api.GetFriends()

def getfriend(friends):
    global f
    global count
    quence=[]
    offset=0

    fhash=[]
    for i in range(0,176):
        fhash.append([])

    while 1:
        for friend in friends:
            sameid=0
            try:                     #check if there is authority to get friend
                api.GetFriends(user=friend.id)
            except:
                continue
        
            if friend.lang !='en':
                continue

            #check if friend id exists
            n=hashfction(friend.id)
            for check in fhash[n]:
                if check==friend.id:
                    sameid=1
                    break
            #if friend id exists, then change to another id
            if sameid==1:
                continue
            #if friend id does not exist, put the id into the file
            quence.append(friend.id)
            strid='%d\n' % friend.id
            f.write(strid)
            count +=1
            print '%s  count=%d  offset=%d' % (friend.screen_name,count,offset)
            if count >= 100000:
                exit(0)

        getfrid=quence[offset]
        offset +=1
        try:
            friends=api.GetFriends(user=getfrid)
        except:
            print 'wierd'


try:
    getfriend(friends)
finally:
    strcount='count=%d' % count
    f.write(strcount)
    f.close()



