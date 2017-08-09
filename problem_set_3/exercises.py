
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
print(stdDevOfLengths(L))
#should return 1.8708.

def getCoefficientOfVariation(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return std/mean

N = [10, 4, 12, 15, 20, 5] 
print(getCoefficientOfVariation(N))