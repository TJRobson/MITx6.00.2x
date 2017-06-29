###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """   

    sorted_cows = sorted(cows.items(), key=lambda cow: cow[1], reverse=True)
    cow_list = []
    
    while len(sorted_cows) > 0:
    
        cow = sorted_cows[0]
        cow_group, cow_sum = [cow[0]], cow[1]
        sorted_cows.remove(cow)
        copy_cl = sorted_cows[:]
       
        for n_c in copy_cl:
       
            if cow_sum + n_c[1] <= limit:
                cow_sum += n_c[1]
                cow_group.append(n_c[0])
                sorted_cows.remove(n_c)
                
        cow_list.append(cow_group)

    return cow_list
# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_copy = cows.copy()
    cow_keys = cows_copy.keys()
    best_trip, L = [], len(cow_keys)   

    for part in get_partitions(cow_keys):
        if len(part) <= L:
            for i, chunk in enumerate(part):            
                weight = sum(cows_copy[c] for c in chunk)               
                if weight <= limit:
                    if i == (len(part)-1):
                        best_trip, L = part, len(part)
                else:
                    break
    return best_trip
    
    
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

#hefs = {'Betsy': 39, 'Abby': 28, 'Willow': 59, 'Rose': 42, 'Buttercup': 11, 'Coco': 59, 'Starlight': 54, 'Luna': 41}
#h = greedy_cow_transport(hefs, 120)
#print(h)
#print(greedy_cow_transport(cows, limit))

start = time.time()
print(brute_force_cow_transport(cows, limit))
end = time.time()
print(end - start)

#print(brute_force_cow_transport({'Daisy': 50, 'Betsy': 65, 'Buttercup': 72, 'Hat': 25}, 75))

