#this will generate the Countdown word
#have integrated this into the countdown-solver script
import random
import string

#generates 3 vowels, 4 cons, and 2 of any as per Countdown rules
vowels = ('a','o','u','e','i')
consonant = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')

randVow = ''.join(random.choice(vowels) for i in range(3))
randCon = ''.join(random.choice(consonant) for i in range(4))  
randAny = ''.join(random.choice(string.ascii_lowercase) for i in range(2)) 

rand = randVow + randCon + randAny
print (rand)





input('Press ENTER to exit') #to keep window open
