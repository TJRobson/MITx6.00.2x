
#Write a function, stdDevOfLengths(L) that takes in a list of strings, L, 
#and outputs the standard deviation of the lengths of the strings.
#Return float('NaN') if L is empty.

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    lens, length = [len(l) for l in L], float(len(L))
    if length == 0:
        return float('NaN')
    
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
