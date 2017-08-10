
#Write a function, stdDevOfLengths(L) that takes in a list of strings, L, 
#and outputs the standard deviation of the lengths of the strings.
#Return float('NaN') if L is empty.

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    length = float(len(L))
    if length == 0:
        return float('NaN')
    lens = [len(l) for l in L]
    mean = sum(lens)/length
    quant = [(m - mean)**2 for m in lens]
    total = sum(quant)
    stdDev = (total/length)**0.5
  
    return stdDev

#Test case: If 
#L = ['a', 'z', 'p']
#print(stdDevOfLengths(L))
#should return 0.

#Test case: If 
L = ['apples', 'oranges', 'kiwis', 'pineapples'] 
#print(stdDevOfLengths(L))
#should return 1.8708.

def getCoefficientOfVariation(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return std/mean

N = [10, 4, 12, 15, 20, 5] 
#print(getCoefficientOfVariation(N))

import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    hits = 0
    for trail in range(numTrials):
        bucket = ['red', 'red', 'red', 'green', 'green', 'green']
        drawn = random.sample(bucket, 3)
        if drawn[0] == drawn[1] == drawn[2]:
            hits += 1
    return float(hits)/float(numTrials)

#def noReplacementSimulation(numTrials):
#    '''
#    Someone else's example single line aproach.
#    Not bad.
#    '''
#    
#    return [random.sample(3*['g','r'],3).count('g')%3 for i in range(numTrials)].count(False)/numTrials

print(noReplacementSimulation(500000))
        
        
    