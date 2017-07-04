#Here is the lecture from 6.00.1x on generators. Additionally, 
# you can also take a look at Chapter 8.3 in the textbook.
#For the following problem, consider the following way to write a power set generator.
#The number of possible combinations to put n items into one bag is 2n. Here, 
#items is a Python list. If need be, also check out the docs on bitwise operators (<<, >>, &, |, ~, ^).

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
#As above, suppose we have a generator that returns every combination of objects in one bag. 
#We can represent this as a list of 1s and 0s denoting whether each item is in the bag or not.

#Write a generator that returns every arrangement of items such that each is in one or none of two different bags.
#Each combination should be given as a tuple of two lists, the first being the items in bag1,
# and the second being the items in bag2.
#def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
#Note this generator should be pretty similar to the powerSet generator above.
#We mentioned that the number of possible combinations for N items into one bag is 2n. 
#How many possible combinations exist when there are two bags? Think about this for a few minutes, 
#then click the following hint to confirm if your guess is correct. 
#Remember that a given item can only be in bag1, bag2, or neither bag 
#-- it is not possible for an item to be present in both bags!


def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    
    for i in range(3**N):
        combo_one, combo_two = [], []   
        for j in range(N):
            if (i // (3**j)) % 3 == 1:
                combo_one.append(items[j])
            elif (i // (3**j)) % 3 == 2:
                combo_two.append(items[j])
                
        yield (combo_one, combo_two)
 
from lecture3Segment2 import Node, Edge, Graph
#Consider our representation of permutations of students in a line from Exercise 1. 
#(The teacher only swaps the positions of two students that are next to each other in line.) 
#Let's consider a line of three students, Alice, Bob, and Carol (denoted A, B, and C). 
#Using the Graph class created in the lecture, we can create a graph with the design chosen in Exercise 1:
#vertices represent permutations of the students in line; edges connect two permutations 
#if one can be made into the other by swapping two adjacent students.

#We construct our graph by first adding the following nodes:

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)
#Add the appropriate edges to the graph.
    
for n_one in nodes:
    n1 = n_one.getName()
    for n_two in nodes:
        n2 = n_two.getName()
        if (n1[:2] == n2[1::-1]) or (n1[1:] == n2[2:0:-1]):
            if not n_two in g.childrenOf(n_one):
                g.addEdge(Edge(n_one, n_two))

print(g)

#Write a WeightedEdge class that extends Edge. Its constructor requires a weight parameter, 
#as well as the parameters from Edge. You should additionally include a getWeight method. 
#The string value of a WeightedEdge from node A to B with a weight of 3 should be "A->B (3)".

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        # Your code here
        return self.weight
    def __str__(self):
        # Your code here
        weight_str = str(self.getWeight())
        return self.src.getName() + '->' + self.dest.getName() + ' (%s)' %(weight_str)

