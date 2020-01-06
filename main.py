import random
import re

words = []

for x in range(7):
    word = input("Please enter a word: ")
    words.append(word.lower())
print(words)
number_to_generate = int(input("How many passwords would you like to generate? "))
is_leet = input("Would you like to use 1773 mode? [y/n]")
for item in range(number_to_generate):
    end_password = ""
    for key in range(random.randint(3,5)):
        end_password += "/" + random.choice('aaaaaaaabbbbccccdefhijk')
    base = random.choice(words)
    end_password = re.sub(r'/a',base,end_password)
    end_password = re.sub(r'/b',base[:len(base) // 2], end_password)
    end_password = re.sub(r'/c',base[len(base)//2:], end_password)
    end_password = re.sub(r'/d',base[:len(base) // 3], end_password)
    end_password = re.sub(r'/e',base[len(base) // 3:(len(base)//3)*2], end_password)
    end_password = re.sub(r'/f',base[len(base) // 3:], end_password)
    end_password = re.sub(r'/h',str(0), end_password)
    end_password = re.sub(r'/i',str(1), end_password)
    end_password = re.sub(r'/j',str(9), end_password)
    end_password = re.sub(r'/k',str(random.randint(0,9)), end_password)
    
    leet_password = ""
    for letter in end_password:
        if letter.lower() in "aceilost" and random.randint(1,10) == 1 and is_leet is "y":
            lletter = letter.replace('a','4').replace('c','(').replace('e','3').replace('i','1').replace('l','1').replace('o','0').replace('s','5').replace('t','7')
            leet_password += lletter
        else:
            leet_password += letter
    upper_password = ""
    for letter in leet_password:
        if random.randint(0,2) == 0:
            upper_password += letter.upper()
        else:
            upper_password += letter
    print(upper_password)