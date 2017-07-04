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
    while True:
        ran = random.randrange(10, 22)
        return ran - ran%2
