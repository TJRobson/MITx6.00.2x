#How would you randomly generate an even number x, 0 <= x < 100? 
#Fill out the definition for the function genEven(). 
#Please generate a uniform distribution over the even numbers between 0 and 100 (not including 100).
import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # Your code here
    return random.randrange(0, 100, 2)

#Write a deterministic program, deterministicNumber, that returns an even number between 9 and 21.

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    return 21 - 9 

#Write a uniformly distributed stochastic program, stochasticNumber, 
#that returns an even number between 9 and 21.

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
   #while True:
        #Does not need while loop
    ran = random.randrange(10, 22)
    return ran - ran%2

print(stochasticNumber())

#The output of random.randint(1, 10) after a specific seed is shown below.
#
#>>> import random
#>>> random.seed(9001)
#>>> random.randint(1, 10)
#1
#>>> random.randint(1, 10)
#3
#>>> random.randint(1, 10)
#6
#>>> random.randint(1, 10)
#6
#>>> random.randint(1, 10)
#7
#We would like you to solve this problem using just the above output, without using the interpreter. 
#(Note that the actual output you get when you run the above commands is actually going to be 1, 5, 5, 2, 10) 
#What is printed in the following programs? Separate new lines with commas 
#- so the above output would be 1, 3, 6, 6, 7.

# answers are based on 1, 3, 6, 6, 7

random.seed(9001)
for i in range(random.randint(1, 10)):
    print(random.randint(1, 10))
# answer: 3
random.seed(9001)
d = random.randint(1, 10)
for i in range(random.randint(1, 10)):
    print(d)
# answer: 1,1,1
random.seed(9001)
d = random.randint(1, 10)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) < 7:
        print(d)
    else:
        random.seed(9001)
        d = random.randint(1, 10)
        print(random.randint(1, 10))
# answer 1,1,3

