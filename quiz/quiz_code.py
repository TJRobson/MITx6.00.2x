
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
    while not i > (len(songs)-1) and space_left < max_size:
        
        temp_size = space_left + songs_cpy[i][2]    
        
        if temp_size <= max_size:
            play_list.append(songs_cpy[i][0])
            space_left = temp_size
            i += 1     
        else:            
            break  
        
    return play_list

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]  
max_size = 12.2
# Returns ['Roar','Wannabe','Timber']

print(song_playlist(songs, max_size))
print(song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 20))
print(song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 11))
print(song_playlist([('aa', 4, 4), ('bb', 5, 7), ('cc', 5, 6), ('dd', 2, 1)], 3))
print(song_playlist([('z', 0.1, 9.0), ('a', 4.4, 5.0), ('b', 2.7, 7.2), ('cc', 3.5, 7.7), ('ddd', 5.1, 6.9)], 14))
