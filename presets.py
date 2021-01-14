
def create_beat_distribution(dist):
    assert (len(dist) == 8), "8 numbers required"
    result = {} 
    for i in range(-4, 3, 1):
        result[beat * 2**i] = i+4
    return result

def create_note_distribution(dist):
    assert (len(dist) == 8), "8 numbers required"
    return list(result)



beat = 480 #common number of beats per quarter

sample_distributions = {
    "default" : create_beat_distribution([0, 0, 1, 8, 16, 5, 3, 2])
}

"""
beat / 16 : 0,    #
beat / 8  : 0,    #
beat / 4  : 1,    # 16th note
beat / 2  : 8,    # Eight note
beat / 1  : 16,   # Quarter in /4 time sig
beat * 2  : 5,    # Half Note
beat * 3  : 3,    # Dotted half 
beat * 4  : 2     # Whole note
"""