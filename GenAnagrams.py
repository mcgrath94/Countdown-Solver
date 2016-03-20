#this will generate the Countdown word

import random
import string

#for now just generates any 9 letter word
# -does not yet meet countdown game requirements
rand = ''.join(random.choice(string.ascii_lowercase) for i in range(9)) 
print (rand)

input('Press ENTER to exit') #to keep window open
