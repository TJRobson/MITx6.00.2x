
def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    play_list, space_left = list(), 0   
    songs_cpy = songs[:1] + sorted(songs[1:], key=lambda x: x[2])
    
    i = 0  
    while i != len(songs) and space_left < max_size:
        
        temp_size = space_left + songs_cpy[i][2]    
        
        if temp_size <= max_size:
            play_list.append(songs_cpy[i][0])
            space_left = temp_size
            i += 1     
        else:            
            break  
        
    return play_list

# Interesting solution to the same problem.

#def song_playlist(songs, max_size):
#    """[...]"""
#    playlist = []
#    try:
#        for (song, length, size) in songs[0:1] \
#                + sorted(songs[1:], key=lambda x: x[2]):
#            if max_size > size:
#                max_size -= size
#                playlist.append(song)
#            else:
#                break
#    except IndexError:
#        pass
#    return playlist

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]  
max_size = 12.2
# Returns ['Roar','Wannabe','Timber']

#print(song_playlist(songs, max_size))
#print(song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 20))
#print(song_playlist([('aa', 4, 4), ('bb', 5, 7), ('cc', 5, 6), ('dd', 2, 1)], 3))
#print(song_playlist([('z', 0.1, 9.0), ('a', 4.4, 5.0), ('b', 2.7, 7.2), ('cc', 3.5, 7.7), ('ddd', 5.1, 6.9)], 14))

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    multipliers, remainder = list(), s
    
    for num in L:
        multipliers.append(remainder // num)
        remainder = remainder % num
    
    return sum(multipliers) if remainder == 0 else 'no solution'
    
print(greedySum([101, 51, 11, 2, 1], 3000), '\n')  
# Answer 36
print(greedySum([30, 20, 10], 60), '\n')
# Answer 2
print(greedySum([10, 9, 8, 1], 17), '\n')
# Answer 8