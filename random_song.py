import mido
import random
from midi_note import Midi_Note
from note import Note
import presets
import util
# See what's less confusing in the end - generating a bunch of notes 
# and then their messages, or generating and working note by note
# Things to consider
#   Repetition
#   Key
#   Pacing in relation to closeby notes 


NOTE_DISTRO_LIST = [4, 7, 8, 3, 8, 1, 2, 3]
REPEAT_DISTRO_LIST = [8, 9, 5, 4, 3, 0, 0, 1]
REPEAT_DISTRO_LIST = [0, 9, 5, 4, 3, 0, 0, 1]

def stringify_list_of_notes(l, sharp=True):
    res = ""
    for note in l:
        res += note.get_note(sharp) + str(note.number) + " "+  str(note.length) + "|"
    return res

def random_note_length(max_len, note_distro):
    res = {}
    for choice, weight in presets.sample_distributions[note_distro].items():
        if choice <= max_len:
            res[choice] = weight
    result = util.weighted_choice(res)
    if result != -1:
        return result
    return max_len 

def rotate_scale_to_note(scale, note):
    result = list(scale)
    while Note(result[0]).get_note()[0] != note.get_note()[0]:
        result.insert(0, result.pop())
    return result

class Melody():
    def __init__(self, channel, **kargs):
        try:
            if kargs["random"]:
                #key, length
                length = kargs["length"]
                note_distro = kargs["note_distro"]
                key = kargs["key"]
                num_beats = length / presets.beat
                
                # def __init__(self, channel, length, velocity, *args):
                note_length = random_note_length(length, note_distro)
                note_number = random.randint(0, 7)
                self.notes = [Midi_Note(channel, note_length, 127, key[note_number])]
                self.length = note_length
                max_length = length - note_length
                while self.length < length:
                    possible_notes = rotate_scale_to_note(key, self.notes[-1])

                    up = random.choice([1, -1])
                    possible_notes = [s + up * 12 for s in possible_notes]
                    note = util.weighted_choice(dict(zip(possible_notes, NOTE_DISTRO_LIST)))
                    next_length = random_note_length(max_length, note_distro) 

                    note_to_append = Midi_Note(channel, next_length, 127, note)
                    self.notes.append(note_to_append)
                    self.length += note_to_append.length
                    max_length = length - self.length
                    if note_length < presets.beat and self.length < length: #repeat
                        if (random.random() > .8):
                            continue
                        repeat_beats = random.choice([1/4, 1/2, 1, 2, 3, 4])
                        total = note_length
                        while total < presets.beat *repeat_beats and self.length < length:
                            possible_notes = rotate_scale_to_note(key, self.notes[-1])
                            up = random.choice([1, -1])
                            possible_notes = [s +   up * 12 for s in possible_notes]


                            note = util.weighted_choice(dict(zip(possible_notes, REPEAT_DISTRO_LIST)))
                            
                            note_to_append = Midi_Note(channel, next_length, 127, note)
                            self.notes.append(note_to_append)
                            self.length += note_to_append.length
                            total += note_length
                #print("62 ----", stringify_list_of_notes(self.notes))
            else:
                pass
        except Exception as E:
            raise E


    def copy(self):
        #????? why is this here?!
        return self

    def write_to_track(self, track):
        for note in self.notes:
            note.start(track)
            note.end(track)

# 1 beat = length=480 

def generate_midi(song_name, time_signature="4/4"):
    time_signature = [int(n) for n in time_signature.split("/")]
    bpm = 170
    channel = 1
    repeat_chance = .5
    measures = 30
    num_tracks = 5
    instruments = [0x07, 0x30]
    distro = ["slow","slow","slow","slow","default"]
    distro = ["slow","slow","slow","slow","slow"]

    #this sets it to C major scale at C3
    scale = "major"
    key = Note("C", 3).scale(scale) 
    key = [n.number for n in key]

    with mido.MidiFile(type=1) as mid:
        info_track = mido.MidiTrack()
        info_track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(bpm)))
        mid.tracks.append(info_track)

        tracks = []
        for n in range(num_tracks):
            channel = n
            tracks.append(mido.MidiTrack())
            track = tracks[-1]
            track.append(mido.MetaMessage('track_name', name="track_" + str(n), time=0))
            track.append(mido.Message('program_change', program=random.randint(0,127), channel=n, time = 0))
            mid.tracks.append(track)

            measure_length = time_signature[1] * presets.beat
            print(n)
            for i in range(measures):
                # going to be used later in more complicated melodies with rests
                progress = 0

                num_melodies = random.choice([1, 2, 4]) # maybe change depending on time signature, 
                                                        # but not working thirds yet
                melody_length = measure_length / num_melodies
                # "energy" and pacing should be around here 
                melodies = [Melody(channel, key=key, note_distro=distro[n],length=melody_length, random=True, scale=scale)]
                for i in range(num_melodies - 1):
                    if (random.random() < repeat_chance):
                        melodies.append((melodies[-1]).copy())
                    else:
                        melodies.append(Melody(channel, key=key, note_distro=distro[n], length=melody_length, random=True, scale=scale))
                for m in melodies:
                    m.write_to_track(track)
                #print("---", i)
            track.append(mido.MetaMessage('end_of_track', time=1))
        mid.save(song_name)

generate_midi("teston.mid")

"""
# Try and find a decent tempo range that holds most songs
# any songs that should be outside can be altered in another program
#mid.ticks_per_beat = random.randint(150, 200)
#mid.ticks_per_beat = 120
key = Note("A", 3).generate_scale("natural minor", True)
key = Note("C", 3).apply_relation("4th", True)
key = Note("C", 3).apply_relation("scale", scale="major")
key = [n.number for n in key]

# For now, only one track
track = mido.MidiTrack()
mid.tracks.append(track)

# 1-96 should be a good number of instrument types
track.append(mido.Message('control_change', channel=10, control=random.randint(0, 95), value=0, time=1))
track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(bpm)))
# 50 random notes for now - later, change to measures if possible 
for i in range(0, 20):
    # Note range for midi is 21-108
    # I haven't actually a clue how tempo and length relates to measures yet
    # default channel = 2
    # no overlapping notes yet
    # def __init__(self, channel, length, velocity, *args):

    # 480  = quarter note
    note = Midi_Note(2, BEAT, 127, random.choice(key)) # find way to write this nicely later
    #print(note.to_string(), note.length) #note = Midi_Note(random.randint(21, 108), random.randint(1, 6) * 48, velocity=127, channel=2) # find way to write this nicely later
    note.start(track)
    note.end(track)

"""

"""
    Notes
        2nd - rare
        chord = should be common if melody? 
        Fourth - read up on what it's supposed to be again but it shouldn't happen too often
        next-note-in-scale = often?
        repeat note = I have a feeling this will have to do mroe with tempo, but give it a scale depending on pacing of the song
        Octave - I don't think often?
            actually, this might be a "calculate, and see if it jumps/falls an octave"
        Play additional note in chord = only if it's on an emphasis beat, then maybe a percentage
        Look up more on how the key of a song affects things and changing it
    For now, since I can handle harmonies okay, focus on melody generating - HOWEVER, for future considerations, consider unsynced chords
        (mainly where the notes are like)
        -------
        ---- 
        or 
        -------
           ----
"""