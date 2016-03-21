#countdown-solver
from itertools import permutations

with open('wordlist.txt', 'r') as f:
    words = {line.strip() for line in f}

test = 'education'

perms = ([''.join(p) for i in range(1, len(test)+1) for p in permutations(test, i)])

#still some issues
#if more than one of certain character, causes duplicates
#also prints all possible words, will modify to print only longest
def main():
    for x in perms:
        if x in words: 
               print(x)

main()

#if you need to keep the window open
#input('Press ENTER to exit') 
