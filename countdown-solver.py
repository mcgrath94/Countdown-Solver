#countdown-solver - now combines the anagram generator and countdown-solver
from itertools import permutations
import random
import string

vowels = ('a','o','u','e','i')
consonant = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')

#generates 3 vowels, 4 cons, and 2 of any as per Countdown rules
randVow = ''.join(random.choice(vowels) for i in range(3))
randCon = ''.join(random.choice(consonant) for i in range(4))  
randAny = ''.join(random.choice(string.ascii_lowercase) for i in range(2)) 

#joins the 3 vowels, 4 cons and other 2 letters
rand = randVow + randCon + randAny
print ('Random letters: ', rand)

with open('wordlist.txt', 'r') as f:
    words = {line.strip() for line in f}


perms = ([''.join(p) for i in range(1, len(rand)+1) for p in permutations(rand, i)])

#still some issues
#if more than one of certain character, causes duplicates
#also prints all possible words, will modify to print only longest
print ('\n---Anagrams--- ')
def main():
    #prints only words that are in perms and in words
    for x in perms:
        if x in words:
            #outputs 9 letter words - if none, then 8, 7...
            #will change with a for loop or something similar
            if len(x)>8:
                print (x)
            elif len(x)>7:
                print (x)
            elif len(x)>6:
                print (x)
            elif len(x)>5:
                print (x)
            elif len(x)>4:
                print (x)

main()

#if you need to keep the window open
#input('Press ENTER to exit') 
